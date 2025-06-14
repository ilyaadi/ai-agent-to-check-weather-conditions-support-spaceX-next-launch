from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self):
        self.name = None
        self.description = None

    @abstractmethod
    async def process(self, input_data):
        """Process input and return enriched data"""
        pass

    def validate_input(self, input_data):
        """Validate input data format"""
        return True
