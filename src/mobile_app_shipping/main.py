#!/usr/bin/env python
import os
import time
import threading
import webbrowser
import re
import json
from typing import List
from flask import Flask, render_template, request
from pydantic import BaseModel, Field
from crewai.flow import Flow, listen, start
from crewai.project import after_kickoff

# === Import your Crews ===
from mobile_app_shipping.crews.app_idea_crew.app_idea_crew import AppIdeaCrew
from mobile_app_shipping.crews.app_design_crew.app_design_crew import AppDesignCrew
from mobile_app_shipping.crews.app_development_crew.app_development_crew import AppDevelopmentCrew


# ======================================
# Flask setup for Human-in-the-Loop UI
# ======================================
app = Flask(__name__)
concepts = []          # stores Crew 1 outputs
selected_concept = ""  # stores user’s selected idea
flow_instance = None   # reference to current Flow instance

class MobileAppConcepts(BaseModel):
    concepts: List[str] = []


class MobileAppFlow(Flow[MobileAppConcepts]):


    @start()
    def kicking_off(self):
        print("🚀 Generating Successful App Ideas...")

    @listen(kicking_off)
    def kicking_off_idea_crew(self):
        """Run Crew 1: App Idea Crew"""
        print("🎨 Running App Idea Crew...")

        app_idea_crew = AppIdeaCrew()
        result = app_idea_crew.crew().kickoff()

        # get the plain text from CrewOutput
        raw_result = result.raw_output if hasattr(result, "raw_output") else str(result)
        print("🧾 Raw LLM output from Crew 1:\n", raw_result[:500])

        # remove markdown fences
        cleaned = re.sub(r"```(?:json)?", "", raw_result).strip()

        parsed_concepts: List[str] = []
        try:
            data = json.loads(cleaned)
            if isinstance(data, dict) and "concepts" in data:
                parsed_concepts = data["concepts"]
            else:
                raise ValueError("JSON missing 'concepts' key")
        except Exception as e:
            print(f"⚠️ JSON parse failed: {e}\nFalling back to text parsing.")
            lines = [re.sub(r"^[\s\-•\*\d\.\)]+", "", l).strip() for l in raw_result.splitlines()]
            parsed_concepts = [l for l in lines if l][:3]

        self.state.concepts = parsed_concepts
        print(f"✅ Parsed {len(parsed_concepts)} concepts for web display.")
        return self.state

    @after_kickoff
    def prep_web_interface(self):
        """Mark that the interface is ready but don't launch Flask here."""
        print("⚙️ Preparing to launch Human-in-the-Loop interface...")
        # just log readiness; we’ll start Flask in kickoff()
        return True

    def resume_after_selection(self, chosen_concept: str):
        """Called by Flask when the human selects a concept."""
        print(f"✅ Human selected: {chosen_concept}\n")

        print("🧠 Running App Design Crew...")
        design_crew = AppDesignCrew()
        design_result = design_crew.crew().kickoff(inputs={"selected_concept": chosen_concept})

        print("💻 Running App Development Crew...")
        dev_crew = AppDevelopmentCrew()
        dev_result = dev_crew.crew().kickoff()

        print("🎉 Workflow complete! Check the web interface for results.\n")
        return design_result, dev_result



# ======================================
# Flask Routes
# ======================================
@app.route('/')
def index():
    # Retrieve structured output from flow state
    global concepts
    if not concepts and flow_instance and flow_instance.state:
        concepts = flow_instance.state.concepts

    if not concepts:
        return "<h2>No app ideas generated yet. Run the flow first.</h2>"

    return render_template("select_concept.html", concepts=concepts)


@app.route("/select", methods=["POST"])
def select():
    global selected_concept
    choice_index = int(request.form["concept"])
    selected_concept = concepts[choice_index]

    design_result, dev_result = flow_instance.resume_after_selection(selected_concept)
    return render_template(
        "result.html",
        concept=selected_concept,
        design_result=design_result,
        dev_result=dev_result,
    )


# ======================================
# Entry Points
# ======================================
def kickoff():
    global flow_instance
    flow_instance = MobileAppFlow()
    flow_instance.kickoff()

    # ✅ Start Flask server after Crew 1 finishes, in a background thread
    def run_flask():
        port = int(os.environ.get("PORT", 5000))
        print(f"🌐 Starting Flask server on http://127.0.0.1:{port}")
        app.run(host="0.0.0.0", port=port, debug=False)

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # ✅ Give Flask a moment to boot before opening browser
    time.sleep(2)

    # Automatically open browser if not production
    if os.environ.get("ENV") != "production":
        try:
            webbrowser.open("http://127.0.0.1:5000")
        except Exception as e:
            print(f"⚠️ Could not open browser automatically: {e}")

    print("✅ Flask server running — open http://127.0.0.1:5000 if it didn't open automatically.\n")

    # Keep main thread alive (since CrewAI flow ended)
    while True:
        time.sleep(5)



def plot():
    flow = MobileAppFlow()
    flow.plot()


if __name__ == "__main__":
    kickoff()