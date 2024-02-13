from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased

from ..Context import SessionMaker
from ..models.FieldOfStudy import FieldOfStudy
from ..models.MVP_API import MVP_API

__fos1 = aliased(FieldOfStudy)
__fos2 = aliased(FieldOfStudy)

def select_fields(session_maker: sessionmaker[Session]=SessionMaker):

    with session_maker() as session:
        fields_pre_query = session \
                                    .query(
                                           MVP_API.field_code,
                                           __fos1.field_name,
                                           __fos2.field_code.label("field_group_code"),
                                           __fos2.field_name.label("field_group_name"),
                                    ) \
                                    .filter(MVP_API.field_code==__fos1.field_code) \
                                    .filter(__fos1.field_group_code==__fos2.field_code) \
                                    .order_by(
                                              __fos2.field_code,
                                              MVP_API.field_code
                                             )


        return fields_pre_query.distinct().all()
