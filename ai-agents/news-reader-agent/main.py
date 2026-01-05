import dotenv

dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class TranslaterCrew:
    @agent
    def translater_agent(self):
        return Agent(
            config=self.agents_config["translater_agent"],
        )
    
    @agent
    def retranslator_agent(self):
        return Agent(
            config=self.agents_config["retranslator_agent"],
        )
    
    @task
    def translate_task(self):
        return Task(
            config=self.tasks_config["translate_task"],
        )
    
    @task
    def retranslate_task(self):
        return Task(
            config=self.tasks_config["retranslate_task"],
        )
    
    @crew
    def assemble_crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
    
TranslaterCrew().assemble_crew().kickoff(inputs={
    "sentence": "Hello, how are you? I hope you have a great day!"
})