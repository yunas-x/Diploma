import json
from pathlib import Path

class InitFromFile():
    
    @classmethod  
    def from_file(cls, path: Path):
        """Initiate schema from file

        Args:
            path (Path): path to Json-schema
        """
        
        with open(path, "r") as file:
            schema = json.load(file)
        
        return cls(schema=schema)
