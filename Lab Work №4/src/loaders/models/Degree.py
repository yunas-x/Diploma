from .BaseModel import BaseModel

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Degree(BaseModel):
    """ORM model for Degree"""
    __tablename__ = "Degree"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=False)
    name: Mapped[str]
    
    curriculae = relationship("Curricula", back_populates="degree")