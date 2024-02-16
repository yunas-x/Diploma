from pydantic import BaseModel, Field, constr
from typing import Optional
from typing import Annotated

from annotated_types import Ge, Le

class ProgramsRequest(BaseModel):
    offset: int = Field(ge=0, default=0)
    limit: int = Field(ge=0, lt=100, default=20)

class Program(BaseModel):
    program_id: int
    program_name: str
    degree_id: int
    degree: str
    field_code: str
    field_name: str
    field_group_code: str
    field_group_name: str

class ProgramsFilter(BaseModel):
    field_code: Optional[list[constr(pattern=r"^[0-5][0-9]\.0[3-5]\.[0-1][1-9]$")]] = Field(default=None)
    degree_id: Optional[list[Annotated[int, Ge(3), Le(5)]]] = Field(default=None)

class ProgramsResponse(ProgramsRequest):
    programs: list[Program]

def programs_from_rows(programs_rows, fields) -> list[Program]:
    
    return [Program(
                    program_id=p.program_id,
                    program_name=p.program_name,
                    degree_id=p.degree_id,
                    degree=p.degree_name,
                    field_code=p.field_code,
                    field_name=fields[p.field_code]["field_name"],
                    field_group_code=fields[p.field_code]["field_group_code"],
                    field_group_name=fields[p.field_code]["field_group_name"]
                   )
            for p
            in programs_rows
	    if p.field_code in fields.keys()]
