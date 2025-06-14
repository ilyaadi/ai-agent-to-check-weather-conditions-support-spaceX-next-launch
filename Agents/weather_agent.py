import os
import aiohttp
from .base_agent import BaseAgent

class WeatherAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.name = "weather"
        self.description = "Weather conditions"
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.api_url = "http://api.openweathermap.org/data/2.5/weather"

    async def process(self, input_data):
        """Process weather data based on launch location"""
        if not input_data.get("location"):
            return {"error": "No location provided from SpaceX data"}

        try:
            params = {
                "q": "Cape Canaveral",  # Default to Cape Canaveral if location parsing fails
                "appid": self.api_key,
                "units": "metric"
            }

            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url, params=params) as response:
                    if response.status != 200:
                        return {"error": "Weather API request failed"}
                    
                    weather_data = await response.json()
                    return {
                        "temperature": weather_data["main"]["temp"],
                        "conditions": weather_data["weather"][0]["description"],
                        "wind_speed": weather_data["wind"]["speed"]
                    }
                    
        except Exception as e:
            return {"error": f"Weather processing failed: {str(e)}"}

    def validate_input(self, input_data):
        """Validate that we have location data"""
        return bool(input_data.get("location"))