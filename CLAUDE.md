# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **CrewAI Flow** application that orchestrates multiple AI agent crews to generate a mobile app concept, design it, and produce Expo/React Native code — with a Flask web UI for human-in-the-loop concept selection.

## Running the App

```bash
# Install dependencies (uses uv)
crewai install

# Run the full flow
crewai run
```

This starts the CrewAI flow (generates 3 app concepts), then launches a Flask server at `http://127.0.0.1:5000` and auto-opens the browser for concept selection.

Environment variables needed in `.env`:
- `OPENAI_API_KEY`, `GEMINI_API_KEY`, `ANTHROPIC_API_KEY`, `HUGGINGFACE_API_KEY`, `SERPER_API_KEY`
- `PORT` — Flask port (default 5000)
- `ENV=production` — set to skip auto-opening the browser

## Architecture

### Flow Execution Order

```
kickoff() → kicking_off_idea_crew() → [Flask UI pauses flow] → resume_after_selection()
```

1. **AppIdeaCrew** — Gemini-powered agents research trending keywords (SerperDevTool) and output exactly 3 app concepts as JSON.
2. **Flask UI** — User selects a concept at `/select`. The POST handler resumes the CrewAI flow.
3. **AppDesignCrew** — Gemini agents produce `app_roadmap.md` and `app_design.md`, plus 4 mockup images via Stable Diffusion XL (Hugging Face).
4. **AppDevelopmentCrew** — Claude Opus agents generate Expo React Native code, run a QA pass, optionally refactor (ConditionalTask), and write `app_code.md`.

### Key Files

- `src/mobile_app_shipping/main.py` — `MobileAppFlow` (CrewAI Flow) + Flask routes + `kickoff()` entry point
- `src/mobile_app_shipping/crews/app_idea_crew/` — Idea generation crew
- `src/mobile_app_shipping/crews/app_design_crew/` — Design + mockup generation crew
- `src/mobile_app_shipping/crews/app_development_crew/` — Code generation + QA crew
- `src/mobile_app_shipping/tools/stable_diffusion_gallery_tool.py` — Custom CrewAI tool that generates 4 screen mockups via Hugging Face API and saves them to `src/mobile_app_shipping/static/`
- `src/mobile_app_shipping/templates/` — Flask HTML templates (`select_concept.html`, `result.html`)

### LLM Assignment

| Crew | LLM |
|------|-----|
| AppIdeaCrew | Gemini 2.0 Flash |
| AppDesignCrew | Gemini 2.0 Flash |
| AppDevelopmentCrew | Claude Opus 4.1 (dev + QA), Gemini (docs) |

### Output Files

Generated files are written to the project root: `app_roadmap.md`, `app_design.md`, `app_code.md`. Mockup images go to `src/mobile_app_shipping/static/app_mockup_*.png`.

### Human-in-the-Loop Pattern

The flow pauses after the idea crew completes. Flask starts in a background daemon thread, and the browser is opened. When the user POSTs to `/select`, the flow's `resume_after_selection()` method is called directly to continue execution.

## Dependency Management

Uses `uv` as the package manager with `pyproject.toml`. The lock file is `uv.lock`. Do not manually edit `uv.lock`.

## Generating the Flow Diagram

```bash
python -c "from mobile_app_shipping.main import plot; plot()"
```

Outputs `crewai_flow.html` — a visual diagram of the flow.
