import json
from pathlib import Path

class InitFromJson:
    
    @classmethod  
    def from_json(cls, path: Path, *args, **kwargs):
        """Initiate object from file
        The class must define the initializer 
        where loaded object should be the first parameter

        Args:
            path (Path): path to Json
        """
        
        with open(path, "r") as file:
            obj: dict = json.load(file)
        
        return cls(obj, *args, **kwargs)
