import os
from job_manager import append_event
from langchain_groq import ChatGroq
from agents import CompanyResearchAgents
from tasks import CompanyResearchTasks
from crewai import Crew


class CompanyResearchCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id
        self.crew = None
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768"
        )

    def setup_crew(self, companies: list[str], positions: list[str]):
        
        # SETUP AGENTS
        agents = CompanyResearchAgents()
        research_manager = agents.research_manager(
            companies, positions
        )
        company_research_agent = agents.company_research_agent()


        # SETUP TASKS
        tasks = CompanyResearchTasks(
            job_id=self.job_id
        )
        company_research_tasks = [
            tasks.company_research(company_research_agent, company, positions) for company in companies
        ]
        manage_research_task = tasks.manage_research(
            research_manager, companies, positions, company_research_tasks
        )

        # CREATE CREW
        self.crew = Crew(
            agents=[research_manager, company_research_agent],
            tasks=[*company_research_tasks, manage_research_task],
            verbose=2,
        )


    def kickoff(self):
        if not self.crew:
            print(f"No crew found for {self.job_id}")

        append_event(self.job_id, "CREW STARTED")
        try:
            print(f"Running crew for {self.job_id}")
            results = self.crew.kickoff()
            append_event(self.job_id, "CREW COMPLETED")
            return results
        
        except Exception as e:
            append_event(self.job_id, f"An error occured: {e}")
            return str(e)