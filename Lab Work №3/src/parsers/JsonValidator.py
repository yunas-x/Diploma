import jsonschema
from mixins.InitFromFileMixin import InitFromFile

from protocols.ValidatorProtocol import ValidatorProtocol

class JsonValidator(ValidatorProtocol, InitFromFile):
    """Validates json file against the schema provided"""
    
    def __init__(self, schema: dict):
        self.schema = schema
    
    def validate(self, data: dict, schema: dict=None) -> bool:
        
        if schema is None:
            schema = self.schema
        
        validator = jsonschema.Draft7Validator(schema=schema)
        return validator.is_valid(data)
