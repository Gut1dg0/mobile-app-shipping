from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.tasks.conditional_task import ConditionalTask
from crewai.tasks.task_output import TaskOutput
from typing import List
from crewai_tools import FileReadTool
from mobile_app_shipping.tools.write_file_tool import write_file
from mobile_app_shipping.tools.zip_project_tool import zip_project
from pathlib import Path
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

def get_project_file_path(filename: str) -> str:
    return str(Path(__file__).resolve().parents[3] / filename)

file_read_tool = FileReadTool(file_path='/Users/agustincompean/Desktop/CrewAI/Flows/mobile_app_shipping/app_design.md')

gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
)

anthropic_llm = LLM(
    model="anthropic/claude-opus-4-1-20250805",
    temperature=0.7,
)

def qa_found_issues(output: TaskOutput) -> bool:
    content = output.output.lower()
    return any(keyword in content for keyword in ["bug", "issue", "improvement"])


@CrewBase
class AppDevelopmentCrew():
    """AppDevelopmentCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def mobile_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['mobile_developer'], # type: ignore[index]
            verbose=True,
            tools=[file_read_tool],
            # llm=gemini_llm,
            allow_delegation=True,
        )

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_engineer'], # type: ignore[index]
            verbose=True,
            # llm=gemini_llm,
        )

    @agent
    def document_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['document_specialist'], # type: ignore[index]
            verbose=True,
            llm=gemini_llm,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def development_task(self) -> Task:
        return Task(
            config=self.tasks_config['development_task'], # type: ignore[index]
        )

    @task
    def qa_task(self) -> Task:
        return Task(
            config=self.tasks_config['qa_task'], # type: ignore[index]
        )

    @task
    def refactoring_task(self) -> ConditionalTask:
        return Task(
            config=self.tasks_config['refactoring_task'], # type: ignore[index]
            condition=qa_found_issues
        )

    @task
    def document_task(self) -> Task:
        return Task(
            config=self.tasks_config['document_task'], # type: ignore[index]
            output_file='app_code.md',
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AppDevelopmentCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
