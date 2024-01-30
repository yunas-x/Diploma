from datetime import timedelta
from datetime import datetime
from typing import Iterable
from sqlalchemy import delete, update
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from ..models.Report import Report
from ..models.Token import Token
from ..models.Intermediate import Intermediate
from ..models.User import User
from .ORMStatus import ORMStatus
from ..models.BaseModel import BaseModel

class Queries:
    """There are DB-queries which are used for CRUD"""

    def __init__(self, session_maker: sessionmaker[Session]):
        self._session_maker = session_maker
    
    def add(self, entity: BaseModel) -> ORMStatus:
        """Add row to DataBase
    
        Args:
            entity (BaseEntityModel): Entity to add
    
        Returns:
            ORMStatus: OK/Fail
        """

        with self._session_maker() as session:
            try:
                session.add(entity)
                session.commit()
                status = ORMStatus.OK
            except Exception as e:
                status = ORMStatus.Fail
                print(e)
        return status
    
    def add_all(self, entities: Iterable[BaseModel]) -> ORMStatus:
        """Add rows to DataBase
    
        Args:
            entities (Iterable[BaseEntityModel]): Entities to add
    
        Returns:
            ORMStatus: OK/Fail
        """

        with self._session_maker() as session:
            try:
                session.add_all(entities)
                session.commit()
                status = ORMStatus.OK
            except:
                status = ORMStatus.Fail
                # There will be logging
        return status
    
    def find_user(self, username: str):
        with self._session_maker() as session:
            id = session \
            .query(User.id) \
            .where(User.username == username) \
            .first()
        return id

    def find_pass(self, username: str, password: str):
        with self._session_maker() as session:
            id = session \
            .query(User.id) \
            .where(User.username == username 
                   and User.password == password) \
            .first()
        return id
    
    def get_reports_by_userid(self, user_id: int):
        with self._session_maker() as session:
            reports = session \
            .query(Report.id,
                   Report.text,
                   Report.posted_on) \
            .where(Report.user_id==user_id) \
            .all()
        return reports
    
    def delete_report_by_id(self, id: int):
        with self._session_maker() as session:
            try:
                session.execute(delete(Report)
                                .where(Report.id == id))
                session.commit()
                status = ORMStatus.OK
            except:
                status = ORMStatus.Fail   
        return status == ORMStatus.OK

    def update_report_by_id(self, id: int, text: str):
        with self._session_maker() as session:
            try:
                session.execute(update(Report)
                                .where(Report.id == id)
                                .values(text=text))
                session.commit()
                status = ORMStatus.OK
            except:
                status = ORMStatus.Fail   
        return status == ORMStatus.OK
    
    def get_programs(self, offset: int=0):
        with self._session_maker() as session:
            programs = session \
            .query(Intermediate.program_name, 
                   Intermediate.degree_id, 
                   Intermediate.field_code,
                   Intermediate.university_id) \
            .distinct(Intermediate.program_name,
                      Intermediate.degree_id, 
                      Intermediate.university_id) \
            .offset(offset) \
            .limit(20) \
            .all()
        return programs
    
    def validate_token(self, user_id: int, token: int):
        since = datetime.now() - timedelta(hours=24)
        with self._session_maker() as session:
            is_valid = session \
                            .query(Token.posted_on) \
                            .where(Token.user_id==user_id and 
                                   Token.token==token and
                                   Token.posted_on) \
                            .filter(Token.posted_on > since) \
                            .count() > 0
        return is_valid