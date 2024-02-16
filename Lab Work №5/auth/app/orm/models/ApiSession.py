from datetime import datetime

from sqlalchemy import func
from .BaseModel import BaseModel

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class ApiSession(BaseModel):
    """ORM model for Session"""
    __tablename__ = "ApiSession"
    
    session_id: Mapped[str] = mapped_column(primary_key=True, index=True, autoincrement=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())


