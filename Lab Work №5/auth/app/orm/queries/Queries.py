from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, desc

import os
from datetime import datetime, timedelta

import uuid
from uuid import uuid5

from ..Context import SessionMaker
from ..models.ApiSession import ApiSession

def add_session(session_maker: sessionmaker[Session]=SessionMaker):

    secret = os.environ['SECRET']
    with session_maker() as session:
        new_session = ApiSession(session_id=str(uuid5(uuid.NAMESPACE_DNS, f"{secret}{datetime.now()}")))
        session.add(new_session)
        session.commit()
        session.refresh(new_session)
    
    return new_session

def get_session(session_id: str, session_maker: sessionmaker[Session]=SessionMaker):

    current_time = datetime.utcnow()
    two_day_ago = current_time - timedelta(hours=48)
    with session_maker() as session:
        api_session = session \
                             .query(ApiSession) \
                             .filter(
                                     and_(
                                          ApiSession.session_id==session_id,
                                          ApiSession.created_at > two_day_ago
                                     )
                             ) \
                             .order_by(desc(ApiSession.created_at)) \
                             .first()
                    
    
    return api_session
