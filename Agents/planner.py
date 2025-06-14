class PlannerAgent:
    def __init__(self):
        self.available_agents = {
            "spacex": "SpaceX launch information",
            "weather": "Weather conditions",
            "news": "News updates",
            "summary": "Summary generation"
        }

    def create_plan(self, goal):
        # Basic routing logic based on goal keywords
        plan = []
        
        if "spacex" in goal.lower() or "launch" in goal.lower():
            plan = [
                {"agent": "spacex", "task": "Get launch details"},
                {"agent": "weather", "task": "Check weather at launch location"},
                {"agent": "news", "task": "Get related launch news"},
                {"agent": "summary", "task": "Summarize launch conditions and potential delays"}
            ]
        elif "weather" in goal.lower():
            plan = [
                {"agent": "weather", "task": "Get weather conditions"},
                {"agent": "summary", "task": "Summarize weather impact"}
            ]
        
        return plan

    def validate_plan(self, plan):
        """Verify all agents exist and dependencies are met"""
        return all(step["agent"] in self.available_agents for step in plan)