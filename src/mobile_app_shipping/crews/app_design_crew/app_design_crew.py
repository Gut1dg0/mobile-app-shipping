from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from mobile_app_shipping.tools.stable_diffusion_gallery_tool import stable_diffusion_gallery
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
)

@CrewBase
class AppDesignCrew():
    """AppDesignCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['business_analyst'], # type: ignore[index]
            verbose=True,
            llm=gemini_llm,
        )

    @agent
    def uxui_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['uxui_designer'], # type: ignore[index]
            verbose=True,
            tools=[stable_diffusion_gallery],
            llm=gemini_llm
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'], # type: ignore[index]
            output_file='app_roadmap.md'
        )

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task'], # type: ignore[index]
            output_file='app_design.md'
        )

    @task
    def image_mockup_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_mockup_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AppDesignCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
