from abc import abstractmethod
from typing import Protocol

class ParserProtocol(Protocol):
    """The uniform interface all parsers shall follow"""
    
    @abstractmethod
    def parse(self, payload) -> dict:
        """Parses raw data into json-serializable dictionary
        
        Returns:
            dict: structured data on university curricula
        """
        pass
    