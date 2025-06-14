import asyncio
import os
from dotenv import load_dotenv
from Agents.planner import PlannerAgent
from Agents.spacex_agent import SpaceXAgent
from Agents.weather_agent import WeatherAgent
from Agents.news_agent import NewsAgent
from Agents.summary_agent import SummaryAgent

class AgentOrchestrator:
    def __init__(self):
        load_dotenv()  # Load environment variables
        self.planner = PlannerAgent()
        self.agents = {
            "spacex": SpaceXAgent(),
            "weather": WeatherAgent(),
            "news": NewsAgent(),
            "summary": SummaryAgent()
        }

    async def execute_plan(self, goal: str) -> dict:
        """Execute the agent plan for a given goal"""
        try:
            # Get plan from planner
            plan = self.planner.create_plan(goal)
            if not self.planner.validate_plan(plan):
                return {"error": "Invalid plan generated"}

            # Execute each step in the plan
            accumulated_data = {}
            for step in plan:
                agent = self.agents.get(step["agent"])
                if not agent:
                    return {"error": f"Agent {step['agent']} not found"}
                
                try:
                    step_result = await agent.process(accumulated_data)
                    accumulated_data.update(step_result)
                except Exception as e:
                    return {"error": f"Agent {step['agent']} failed: {str(e)}"}

            return accumulated_data

        except Exception as e:
            return {"error": f"Orchestration failed: {str(e)}"}

async def main():
    try:
        orchestrator = AgentOrchestrator()
        goal = "Find the next SpaceX launch and check if weather might delay it"
        
        print(f"Processing goal: {goal}")
        result = await orchestrator.execute_plan(goal)
        
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("\nFinal Summary:")
            print(result.get("summary", "No summary generated"))
            print(f"Launch Feasibility: {result.get('launch_feasibility', 'Unknown')}")

    except Exception as e:
        print(f"Application error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())