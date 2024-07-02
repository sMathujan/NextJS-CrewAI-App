from job_manager import append_event


class CompanyResearchCrew:
    def __init__(self, job_id: str):
        self.job_id = job_id
        self.crew = None

    def setup_crew(self, companies: list[str], positions: list[str]):
        print(f"Setting up crew for {self.job_id} with companies {companies} and positions {positions}.")

        # TODO: SETUP AGENTS
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