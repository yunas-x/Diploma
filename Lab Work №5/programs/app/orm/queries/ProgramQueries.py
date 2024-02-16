from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from ..Context import SessionMaker
from ..models.Degree import Degree
from ..models.MVP_API import MVP_API

def build_filters(filter: Optional[dict[str, list]]=None):
    filters_templates = {
        "degree_id": MVP_API.degree_id.in_,
        "field_code": MVP_API.field_code.in_,
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
                                           MVP_API.degree_id,
			                               Degree.name.label("degree_name")
			                        ) \
                                    .filter(MVP_API.degree_id==Degree.id) \

        orm_filter = build_filters(filter)
        if orm_filter:
            programs_pre_query = programs_pre_query.filter(*orm_filter)

        programs = programs_pre_query \
                                     .offset(offset) \
                                     .limit(limit) \
                                     .all()

    return programs

def select_fields(session_maker: sessionmaker[Session]=SessionMaker):

    with session_maker() as session:
        fields_pre_query = session.query(MVP_API.field_code).distinct()
        fields = fields_pre_query.all()

    return fields

