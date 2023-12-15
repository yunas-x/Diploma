from typing import List

from loaders.models.BaseModel import BaseModel

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Course(BaseModel):
    """ORM model for Course"""
    __tablename__ = "Course"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    type: Mapped[str]
    
    curricula = relationship("Curricula", back_populates="courses")