from .BaseModel import BaseModel

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class User(BaseModel):
    """ORM model for University"""
    __tablename__ = "User"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(index=True)
    email: Mapped[str]
    password: Mapped[str]
    
    reports = relationship("Report", back_populates="user")