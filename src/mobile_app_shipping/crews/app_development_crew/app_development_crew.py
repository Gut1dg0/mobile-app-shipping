import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.tasks.conditional_task import ConditionalTask
from crewai.tasks.task_output import TaskOutput
from typing import List
from crewai_tools import FileReadTool

claude_llm = LLM(
    model="anthropic/claude-sonnet-4-6",
    temperature=0.2,
)

ollama_llm = LLM(
    model="ollama/qwen2.5:7b",
    base_url="http://localhost:11434",
    temperature=0.7,
)

gemini_llm = LLM(
    model="google/gemini-3.1-pro-preview",
    temperature=0.7,
)


def qa_found_issues(output: TaskOutput) -> bool:
    content = output.output.lower()
    return not content.startswith("lgtm") and any(
        keyword in content for keyword in ["bug", "issue", "error", "fix", "problem", "missing", "incorrect", "invalid"]
    )


@CrewBase
class AppDevelopmentCrew():
    """AppDevelopmentCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def mobile_developer(self) -> Agent:
        file_path = os.path.join(os.getcwd(), 'app_design.md')
        file_read_tool = FileReadTool(file_path=file_path)
        return Agent(
            config=self.agents_config['mobile_developer'], # type: ignore[index]
            verbose=True,
            tools=[file_read_tool],
            llm=ollama_llm,
            allow_delegation=True,
        )

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_engineer'], # type: ignore[index]
            verbose=True,
            llm=ollama_llm,
        )

    @agent
    def document_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['document_specialist'], # type: ignore[index]
            verbose=True,
            llm=ollama_llm,
        )

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
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
