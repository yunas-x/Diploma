from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased

from ..Context import SessionMaker
from ..models.FieldOfStudy import FieldOfStudy

__fos1 = aliased(FieldOfStudy)
__fos2 = aliased(FieldOfStudy)

def select_fields(fields_codes_filter: list[str]=None, session_maker: sessionmaker[Session]=SessionMaker):

    with session_maker() as session:
        fields_pre_query = session \
                                    .query(
                                           __fos1.field_code,
                                           __fos1.field_name,
                                           __fos2.field_code.label("field_group_code"),
                                           __fos2.field_name.label("field_group_name"),
                                    ) \
                                    .filter(__fos1.field_group_code==__fos2.field_code) \
                                    .order_by(
                                              __fos2.field_code,
                                              __fos1.field_code
                                             )
        
        if fields_codes_filter:
            fields_pre_query = fields_pre_query.filter(__fos1.field_code.in_(fields_codes_filter))
            
        return fields_pre_query.distinct().all()
