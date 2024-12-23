from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from dotenv import load_dotenv

load_dotenv()


@CrewBase
class CompetitorAnalyst():
	"""CompetitorAnalyst crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	llm = LLM(
		model='ollama/llama3.1:8b',
		base_url='http://localhost:11434',
	)

	@agent
	def input_processing_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['input_processing'],
			verbose=True,
			llm = self.llm,
			tools =[SerperDevTool(n_results=2),
					ScrapeWebsiteTool()
			]
		)

	@agent
	def data_retrieval_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['data_retrieval'],
			verbose=True,
			llm = self.llm,
			tools =[SerperDevTool(),
					ScrapeWebsiteTool()
			]
		)

	@agent
	def data_processing_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['data_processing'],
			verbose=True,
			llm = self.llm,
		)

	@agent
	def feature_comparison_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['feature_comparison'],
			verbose=True,
			llm = self.llm,
		)
	
	@agent
	def risk_assessment_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['risk_assessment'],
			verbose=True,
			llm=self.llm,
		)

	@agent
	def swot_analysis_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['swot_analysis'],
			verbose=True,
			llm = self.llm,
		)

	@agent
	def report_generation_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['report_generation'],
			verbose=True,
			llm = self.llm
		)


############# task ################

	@task
	def input_processing_task(self) -> Task:
		return Task(
			config=self.tasks_config['input_processing_task'],
		)
	
	@task
	def data_retrieval_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_retrieval_task'],
		)

	@task
	def data_processing_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_processing_task'],
		)

	@task
	def feature_comparison_task(self) -> Task:
		return Task(
			config=self.tasks_config['feature_comparison_task'],
		)
	
	@task
	def risk_assessment_task(self) -> Task:
		return Task(
			config=self.tasks_config['risk_assessment_task'],
		)
	
	@task
	def swot_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['swot_analysis_task'],
		)

	@task
	def report_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['report_generation_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CompetitorAnalyst crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
