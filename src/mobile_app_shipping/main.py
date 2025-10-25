#!/usr/bin/env python
from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from mobile_app_shipping.crews.app_idea_crew.app_idea_crew import AppIdeaCrew

from mobile_app_shipping.crews.app_development_crew.app_development_crew import AppDevelopmentCrew


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


def kickoff():
    app_flow = MobileAppFlow()
    app_flow.kickoff()


def plot():
    app_flow = MobileAppFlow()
    app_flow.plot()


if __name__ == "__main__":
    kickoff()
