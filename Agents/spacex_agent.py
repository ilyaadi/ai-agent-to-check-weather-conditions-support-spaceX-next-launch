import aiohttp
from .base_agent import BaseAgent

class SpaceXAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.name = "spacex"
        self.description = "SpaceX launch information"
        self.api_url = "https://api.spacexdata.com/v4/launches/next"

    async def process(self, input_data):
        """Get next SpaceX launch information"""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:
                launch_data = await response.json()
                return {
                    "launch_date": launch_data["date_utc"],
                    "location": launch_data["launchpad"],
                    "mission": launch_data["name"]
                }

    def validate_input(self, input_data):
        """No input required for SpaceX next launch query"""
        return True