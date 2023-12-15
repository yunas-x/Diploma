from typing import List

from sqlalchemy import ForeignKey

from loaders.models.BaseModel import BaseModel

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Curricula(BaseModel):
    """ORM model for Curricula"""
    __tablename__ = "Curricula"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("Course.id"))
    credits: Mapped[int]
    classroom_hours: Mapped[int]
    # there will be more 
    
    courses = relationship("Course", back_populates="curricula")