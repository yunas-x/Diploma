import datetime
from typing import Optional

from .BaseModel import BaseModel


from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class IntermediateValues(BaseModel):
    """ORM model for IntermediateValues"""
    __tablename__ = "IntermediateValues"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    course_name: Mapped[str]
    program_name: Mapped[str]
    enrollment_year: Mapped[int] = mapped_column(index=True)
    year: Mapped[int] = mapped_column(index=True)
    credits: Mapped[int]
    classroom_hours: Mapped[Optional[int]]
    readBy: Mapped[str]
    