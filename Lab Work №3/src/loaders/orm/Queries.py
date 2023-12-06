from typing import Iterable
from sqlalchemy.orm import Session

from loaders.models.BaseModel import BaseModel
from loaders.orm.ORMStatus import ORMStatus

def add(session: Session, entity: BaseModel) -> ORMStatus:
    """Add row to DataBase

    Args:
        session (Session): DataBase Session (might be injected through SessionMaker)
        entity (BaseEntityModel): Entity to add

    Returns:
        ORMStatus: OK/Fail
    """
    try:
        session.add(entity)
        session.commit()
        status = ORMStatus.OK
    except:
        status = ORMStatus.Fail
        # There will be logging
    finally:
        session.close()
        
    return status

def add_all(session: Session, entities: Iterable[BaseModel]) -> ORMStatus:
    """Add rows to DataBase

    Args:
        session (Session): DataBase Session (might be injected through SessionMaker)
        entities (Iterable[BaseEntityModel]): Entities to add

    Returns:
        ORMStatus: OK/Fail
    """
    try:
        session.add_all(entities)
        session.commit()
        status = ORMStatus.OK
    except:
        status = ORMStatus.Fail
        # There will be logging
    finally:
        session.close()
        
    return status