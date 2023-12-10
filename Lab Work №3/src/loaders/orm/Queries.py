from typing import Iterable
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from loaders.models.BaseModel import BaseModel
from loaders.orm.ORMStatus import ORMStatus

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
            except:
                status = ORMStatus.Fail
                # There will be logging
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
