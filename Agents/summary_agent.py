from .base_agent import BaseAgent

class SummaryAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.name = "summary"
        self.description = "Summary generation"

    async def process(self, input_data):
        """
        Generate summary based on all previous agent data
        Expected input_data format:
        {
            "mission": str,            # From SpaceX
            "launch_date": str,        # From SpaceX
            "temperature": float,      # From Weather
            "conditions": str,         # From Weather
            "wind_speed": float,       # From Weather
            "news_articles": list      # From News
        }
        """
        if not self.validate_input(input_data):
            return {"error": "Insufficient data for summary"}

        # Analyze weather conditions for launch
        weather_status = self._analyze_weather_conditions(
            input_data["temperature"],
            input_data["wind_speed"],
            input_data["conditions"]
        )

        # Generate summary
        summary = (
            f"SpaceX mission '{input_data['mission']}' is scheduled for {input_data['launch_date']}. "
            f"Weather conditions: {weather_status}. "
        )

        # Add news context if available
        if input_data.get("news_articles"):
            latest_news = input_data["news_articles"][0]
            summary += f"Latest related news: {latest_news['title']}"

        return {
            "summary": summary,
            "launch_feasibility": "favorable" if "unfavorable" not in weather_status else "uncertain"
        }

    def _analyze_weather_conditions(self, temperature, wind_speed, conditions):
        """Analyze weather conditions for launch feasibility"""
        concerns = []

        if wind_speed > 20:  # m/s
            concerns.append("high winds")
        if "Rain" in conditions or "Storm" in conditions:
            concerns.append("precipitation")
        if temperature < -5 or temperature > 35:  # Celsius
            concerns.append("extreme temperature")

        if not concerns:
            return "favorable for launch"
        return f"potentially unfavorable due to {', '.join(concerns)}"

    def validate_input(self, input_data):
        """Verify all required fields are present"""
        required_fields = [
            "mission", "launch_date", "temperature",
            "conditions", "wind_speed"
        ]
        return all(field in input_data for field in required_fields)