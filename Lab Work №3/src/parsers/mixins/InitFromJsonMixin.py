import json
from pathlib import Path

class InitFromJson():
    
    @classmethod  
    def from_json(cls, path: Path, **kwargs):
        """Initiate object from file

        Args:
            path (Path): path to Json
        """
        
        with open(path, "r") as file:
            schema = json.load(file)
        
        return cls(schema=schema, kwargs)
