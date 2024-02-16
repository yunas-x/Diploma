from pydantic import BaseModel

class FieldOfStudy(BaseModel):
    field_code: str
    field_name: str
    field_group_code: str
    field_group_name: str

def fields_from_rows_grouped(fields_rows) -> list[FieldOfStudy]:
    return [FieldOfStudy(
                         field_code=f.field_code,
                         field_name=f.field_name,
                         field_group_code=f.field_group_code,
                         field_group_name=f.field_group_name
                 )
            for f
            in fields_rows]
