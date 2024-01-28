import datetime
import enum
from typing import Optional

from .BaseModel import BaseModel

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class CourseType(enum.Enum):
    MANDATORY = "Обязательный"
    ELECTIVE = "По выбору"
    FACULTATIVE = "Факультативный"

class Course(BaseModel):
    """ORM model for Course"""
    __tablename__ = "Course"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    type: Mapped[CourseType] = mapped_column(index=True)
    added: Mapped[Optional[datetime.date]]
    removed: Mapped[Optional[datetime.date]]
    
    curriculae = relationship("Curricula", back_populates="courses")