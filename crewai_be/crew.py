from job_manager import append_event
from agents import CompanyResearchAgents


class CompanyResearchCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id
        self.crew = None

    def setup_crew(self, companies: list[str], positions: list[str]):
        
        agents = CompanyResearchAgents()

        research_manager = agents.research_manager(
            companies, positions
        )
        company_research_agent = agents.company_research_agent()


        # TODO: SETUP TASKS
        # TODO: CREATE CREW

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