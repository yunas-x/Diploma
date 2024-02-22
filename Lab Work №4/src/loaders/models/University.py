from .BaseModel import BaseModel

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class University(BaseModel):
    """ORM model for University"""
    __tablename__ = "University"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    
    curriculae = relationship("Curricula", back_populates="university")