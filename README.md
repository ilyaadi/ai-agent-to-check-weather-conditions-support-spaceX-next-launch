# Multi-Agent AI System

A modular multi-agent system that orchestrates different AI agents to achieve complex goals using public APIs. The system takes a user goal, creates an execution plan, and chains multiple agents together to process and enrich data.

## Features

- 🤖 Modular agent architecture
- 📋 Dynamic task planning
- 🔄 Sequential data enrichment
- 🌐 Multiple API integrations (SpaceX, OpenWeather, NewsAPI)
- ⚙️ Configurable settings
- 📊 Performance monitoring

## Project Structure

```
AI Agent/
├── Agents/
│   ├── base_agent.py     # Base class for all agents
│   ├── planner.py        # Plans execution sequence
│   ├── spacex_agent.py   # SpaceX launch data
│   ├── weather_agent.py  # Weather conditions
│   ├── news_agent.py     # News fetching
│   └── summary_agent.py  # Data summarization
├── tests/               # Test suite
├── config.py           # Configuration management
├── metrics.py          # Performance monitoring
└── main.py            # Main orchestrator
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-agent.git
cd ai-agent
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create .env file with your API keys
```env
OPENWEATHER_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
```

## Usage

Run the main script:
```bash
python main.py
```

Example goal:
```python
"Find the next SpaceX launch and check if weather might delay it"
```

## Agent Flow

1. PlannerAgent creates execution plan
2. SpaceXAgent fetches launch details
3. WeatherAgent checks conditions
4. NewsAgent gathers related news
5. SummaryAgent combines all data

## Requirements

- Python 3.8+
- aiohttp
- pydantic
- python-dotenv
- tenacity

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Acknowledgments

- SpaceX API
- OpenWeather API
- NewsAPI
