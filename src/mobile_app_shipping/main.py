#!/usr/bin/env python
import os
import threading
import re
import json
from typing import List
from flask import Flask, render_template, send_from_directory, request, jsonify, redirect, url_for
from pydantic import BaseModel
from crewai.flow import Flow, listen, start

from mobile_app_shipping.crews.app_idea_crew.app_idea_crew import AppIdeaCrew
from mobile_app_shipping.crews.app_design_crew.app_design_crew import AppDesignCrew
from mobile_app_shipping.crews.app_development_crew.app_development_crew import AppDevelopmentCrew


# ======================================
# Flask app + global flow state
# ======================================
app = Flask(__name__)

# Thread-safe state shared between Flask and the flow thread
_lock = threading.Lock()
_state = {
    "status": "idle",   # idle | generating_ideas | awaiting_selection | designing | developing | complete | error
    "message": "Ready. Click Launch to start.",
    "concepts": [],
    "selected_concept": None,
    "error": None,
}


def _set_state(**kwargs):
    with _lock:
        _state.update(kwargs)


def _get_state():
    with _lock:
        return dict(_state)


# ======================================
# CrewAI Flow (idea generation only)
# ======================================
class MobileAppConcepts(BaseModel):
    concepts: List[str] = []


class MobileAppFlow(Flow[MobileAppConcepts]):

    @start()
    def kicking_off(self):
        _set_state(status="generating_ideas", message="Agents are researching trending app ideas…")

    @listen(kicking_off)
    def kicking_off_idea_crew(self):
        result = AppIdeaCrew().crew().kickoff()
        raw = result.raw if hasattr(result, "raw") else str(result)

        parsed: List[str] = []
        try:
            match = re.search(r"\{[\s\S]*?\}", raw)
            if not match:
                raise ValueError("No JSON block found")
            data = json.loads(match.group(0))
            if isinstance(data, dict) and "concepts" in data:
                parsed = data["concepts"]
            else:
                raise ValueError("Missing 'concepts' key")
        except Exception:
            lines = [re.sub(r"^[\s\-•\*\d\.\)]+", "", l).strip() for l in raw.splitlines()]
            parsed = [l for l in lines if len(l) > 10][:3]

        self.state.concepts = parsed
        _set_state(
            status="awaiting_selection",
            message="3 app concepts are ready — choose one to continue.",
            concepts=parsed,
        )


def _scaffold_flutter_project(app_code_path: str, output_dir: str) -> int:
    """
    Parse app_code.md for === FILE: path === / === END FILE === blocks
    and write each file into output_dir, creating subdirectories as needed.
    Returns the number of files written.
    """
    try:
        with open(app_code_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return 0

    file_pattern = re.compile(
        r'===\s*FILE:\s*(.+?)\s*===\n(.*?)===\s*END FILE\s*===',
        re.DOTALL
    )
    matches = file_pattern.findall(content)

    if not matches:
        return 0

    os.makedirs(output_dir, exist_ok=True)
    count = 0
    for rel_path, file_content in matches:
        rel_path = rel_path.strip()
        full_path = os.path.join(output_dir, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(file_content.strip() + '\n')
        count += 1
    return count


_SETUP_INSTRUCTIONS_TEMPLATE = """\
# Flutter App — Setup & Run Instructions

## Prerequisites

1. **Flutter SDK** (3.x or later)
   Install: https://docs.flutter.dev/get-started/install
   Verify:  `flutter doctor`

2. An **Android emulator** (via Android Studio) or a connected physical device.
   iOS testing requires macOS + Xcode.

## Steps

```bash
# 1 — Navigate into the generated project
cd flutter_app

# 2 — Fetch all dependencies declared in pubspec.yaml
flutter pub get

# 3 — Run the app (picks the first available device/emulator)
flutter run

# To target a specific platform:
flutter run -d android   # Android emulator or device
flutter run -d ios       # iOS simulator (macOS only)
flutter run -d chrome    # Web (if web support is enabled)
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `flutter doctor` reports issues | Follow the doctor's recommendations |
| No devices found | Start an emulator in Android Studio or connect a device |
| Dependency errors | Run `flutter pub upgrade` then retry `flutter run` |
| Build errors | Check that your Flutter SDK version satisfies `sdk: '>=3.0.0 <4.0.0'` |

## Project Structure

```
flutter_app/
  pubspec.yaml        — project manifest & dependencies
  lib/
    main.dart         — app entry point
    screens/          — one file per screen
    widgets/          — reusable widget components
```
"""


def _run_design_and_dev(chosen_concept: str):
    """Runs design + development crews in a background thread."""
    try:
        _set_state(
            status="designing",
            message="Designing app architecture, UX flows, and generating screen mockups…",
            selected_concept=chosen_concept,
        )
        AppDesignCrew().crew().kickoff(inputs={"selected_concept": chosen_concept})

        _set_state(status="developing", message="Writing Flutter code and running QA review…")
        AppDevelopmentCrew().crew().kickoff()

        # Scaffold the real Flutter project from app_code.md
        app_code_path = os.path.join(_PROJECT_ROOT, 'app_code.md')
        flutter_dir = os.path.join(_PROJECT_ROOT, 'flutter_app')
        files_written = _scaffold_flutter_project(app_code_path, flutter_dir)

        # Write setup instructions
        instructions_path = os.path.join(_PROJECT_ROOT, 'SETUP_INSTRUCTIONS.md')
        with open(instructions_path, 'w', encoding='utf-8') as f:
            f.write(_SETUP_INSTRUCTIONS_TEMPLATE)

        if files_written > 0:
            _set_state(
                status="complete",
                message=f"Your Flutter app is ready! {files_written} files written to flutter_app/",
            )
        else:
            _set_state(
                status="complete",
                message="Your app is ready! (See app_code.md — automatic scaffolding found no file delimiters)",
            )

    except Exception as exc:
        _set_state(status="error", message=f"Pipeline error: {exc}", error=str(exc))


# ======================================
# Flask Routes
# ======================================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/start", methods=["POST"])
def api_start():
    state = _get_state()
    if state["status"] not in ("idle", "error", "complete"):
        return jsonify({"error": "Flow is already running"}), 400

    _set_state(
        status="generating_ideas",
        message="Starting AI agents…",
        concepts=[],
        selected_concept=None,
        error=None,
    )

    def _run():
        try:
            MobileAppFlow().kickoff()
        except Exception as exc:
            _set_state(status="error", message=str(exc), error=str(exc))

    threading.Thread(target=_run, daemon=True).start()
    return jsonify({"status": "started"})


@app.route("/api/status")
def api_status():
    return jsonify(_get_state())


@app.route("/loading")
def loading():
    return render_template("loading.html")


@app.route("/select", methods=["GET"])
def select_page():
    state = _get_state()
    if state["status"] != "awaiting_selection":
        return redirect(url_for("loading"))
    return render_template("select_concept.html", concepts=state["concepts"])


@app.route("/select", methods=["POST"])
def select():
    state = _get_state()
    concepts = state["concepts"]
    chosen = concepts[int(request.form["concept"])]
    threading.Thread(target=_run_design_and_dev, args=(chosen,), daemon=True).start()
    return redirect(url_for("loading"))


@app.route("/result")
def result():
    state = _get_state()
    if state["status"] != "complete":
        return redirect(url_for("loading"))
    return render_template("result.html", concept=state["selected_concept"])


# Static file helpers
_STATIC = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))


@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(_STATIC, filename)


@app.route("/downloads/<path:filename>")
def serve_download(filename):
    return send_from_directory(_PROJECT_ROOT, filename, as_attachment=True)


# ======================================
# Entry Points
# ======================================

def kickoff():
    port = int(os.environ.get("PORT", 7860))
    print(f"🌐  Open http://0.0.0.0:{port} to launch the AI pipeline")
    app.run(host="0.0.0.0", port=port, debug=False)


def plot():
    MobileAppFlow().plot()


if __name__ == "__main__":
    kickoff()
