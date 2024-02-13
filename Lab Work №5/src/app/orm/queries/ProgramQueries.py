from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased

from ..Context import SessionMaker
from ..models.FieldOfStudy import FieldOfStudy
from ..models.Degree import Degree
from ..models.MVP_API import MVP_API

__fos1 = aliased(FieldOfStudy)
__fos2 = aliased(FieldOfStudy)

def build_filters(filter: Optional[dict[str, list]]=None):
    filters_templates = {
        "degree_id": MVP_API.degree_id.in_,
        "field_code": MVP_API.field_code.in_,
        "field_group_code": __fos2.field_code.in_
    }

    if not filter:
        return None

    return [filters_templates[f](filter[f])
            for f
            in filter]

def select_programs(filter: Optional[dict[str, list]]=None,
                    session_maker: sessionmaker[Session]=SessionMaker,
		    offset: int=0,
		    limit: int=20):

    with session_maker() as session:
        programs_pre_query = session \
                                    .query(
                                           MVP_API.program_id,
			                   MVP_API.program_name,
			                   MVP_API.field_code,
			                   __fos1.field_name,
			                   __fos2.field_code.label("field_group_code"),
                                           __fos2.field_name.label("field_group_name"),
                                           MVP_API.degree_id,
			                   Degree.name.label("degree_name")
			            ) \
                                    .filter(MVP_API.degree_id==Degree.id) \
                                    .filter(MVP_API.field_code==__fos1.field_code) \
                                    .filter(__fos1.field_group_code==__fos2.field_code)

        orm_filter = build_filters(filter)
        if orm_filter:
            programs_pre_query = programs_pre_query.filter(*orm_filter)

        programs = programs_pre_query \
                                     .offset(offset) \
                                     .limit(limit) \
                                     .all()

    return programs
