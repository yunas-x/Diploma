from abc import abstractmethod
from typing import Protocol

class ValidatorProtocol(Protocol):
    """The uniform interface all data validators shall follow"""
    
    @abstractmethod
    def validate(self, data: dict, schema: dict) -> bool:
        """Check if parsed data complies with schema
        
        Returns:
            bool: True if valid, otherwise False
        """
        raise NotImplementedError
    
