import os
import aiohttp
from .base_agent import BaseAgent

class NewsAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.name = "news"
        self.description = "News information"
        self.api_key = os.getenv("NEWS_API_KEY")
        self.api_url = "https://newsapi.org/v2/everything"

    async def process(self, input_data):
        """
        Process news based on previous agent data
        Expected input_data format:
        {
            "mission": "string",  # From SpaceX agent
            "launch_date": "string"
        }
        """
        if not input_data.get("mission"):
            return {"error": "No mission information provided"}

        query = f"SpaceX {input_data['mission']}"
        params = {
            "q": query,
            "apiKey": self.api_key,
            "sortBy": "publishedAt",
            "language": "en",
            "pageSize": 3
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url, params=params) as response:
                news_data = await response.json()
                
                if news_data["status"] != "ok":
                    return {"error": "Failed to fetch news"}

                articles = news_data["articles"]
                return {
                    "news_articles": [
                        {
                            "title": article["title"],
                            "url": article["url"],
                            "published_at": article["publishedAt"]
                        }
                        for article in articles
                    ]
                }

    def validate_input(self, input_data):
        """Validate required input fields"""
        return bool(input_data.get("mission"))