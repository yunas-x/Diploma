from pydantic import BaseModel

from ...loaders.orm.Queries import Queries
from ...loaders.Context import SessionMaker

class Program(BaseModel):
    program_name: str
    degree_id: int
    field_code: str
    university_id: int
    
class ProgramsResponse(BaseModel):
    offset: int
    programs: list[Program]
    
def get_programs(offset: int) -> list[Program]:
    programs = Queries(SessionMaker).get_programs(offset)
    programs_list = [Program(p.program_name, 
                    p.degree_id, 
                    p.field_code, 
                    p.university_id) 
                    for p in programs]
    return ProgramsResponse(offset=offset, 
                            programs=programs_list)
    