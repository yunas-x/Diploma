from pydantic import BaseModel

class Field(BaseModel):
    field_code: str
    
class FieldsResponse(BaseModel):
    field_codes: list[Field]

def fields_from_rows(field_rows) -> list[Field]:
    return [Field(field_code=f.field_code)
            for f
            in field_rows]
