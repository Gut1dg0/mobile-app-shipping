#!/usr/bin/env python
from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from mobile_app_shipping.crews.app_idea_crew.app_idea_crew import AppIdeaCrew

from mobile_app_shipping.crews.app_development_crew.app_development_crew import AppDevelopmentCrew

import os

import subprocess


class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""


class MobileAppFlow(Flow):

    @start()
    def kicking_off(self):
        print("Generating Succesful App idea")

    @listen(kicking_off)
    def kicking_off_idea_crew(self):
        app_idea_crew = AppIdeaCrew()
        app_idea_crew.crew().kickoff()

    @listen(kicking_off_idea_crew)
    def kicking_off_development_crew(self):
        app_dev_crew = AppDevelopmentCrew()
        app_dev_crew.crew().kickoff()

    @listen(kicking_off_development_crew)
    def wrapping_up(self):
        print("Congratulations and take a look at the code")

    # @listen(wrapping_up)
    # def on_crew_complete(output):
    #     """
    #     Listener that triggers automatically when the crew finishes.
    #     It extracts the project directory and triggers the Expo .aab build.
    #     """
    #     print("\n🚀 App Development Crew has completed successfully!")
    #     print("Output summary:\n", output)

    #     # Parse project_dir from JSON-like output (safe parsing)
    #     if isinstance(output, str) and "project_dir" in output:
    #         import re, json

    #         try:
    #             match = re.search(r'\{.*\}', output, re.DOTALL)
    #             data = json.loads(match.group()) if match else {}
    #             project_dir = data.get("project_dir")
    #         except Exception:
    #             project_dir = None
    #     elif isinstance(output, dict):
    #         project_dir = output.get("project_dir")
    #     else:
    #         project_dir = None

    #     if not project_dir or not os.path.exists(project_dir):
    #         print("❌ Could not find project directory. Skipping .aab build.")
    #         return

    #     print(f"✅ Found project directory: {project_dir}")
    #     print("🏗️ Starting Expo .aab build...")

    #     try:
    #         subprocess.run(["eas", "--version"], check=True, capture_output=True)
    #     except subprocess.CalledProcessError:
    #         print("❌ EAS CLI not installed. Install with: npm install -g eas-cli")
    #         return

    #     try:
    #         process = subprocess.run(
    #             ["eas", "build", "--platform", "android", "--type", "app-bundle", "--non-interactive"],
    #             cwd=project_dir,
    #             text=True,
    #             capture_output=True,
    #         )
    #         if process.returncode == 0:
    #             print("✅ Expo build successfully triggered!")
    #         else:
    #             print("❌ Expo build failed:\n", process.stderr)
    #     except Exception as e:
    #         print(f"❌ Unexpected error during build: {str(e)}")


def kickoff():
    app_flow = MobileAppFlow()
    app_flow.kickoff()


def plot():
    app_flow = MobileAppFlow()
    app_flow.plot()


if __name__ == "__main__":
    kickoff()
