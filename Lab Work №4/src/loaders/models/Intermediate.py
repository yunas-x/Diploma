import datetime
from typing import Optional

from .BaseModel import BaseModel


from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Intermediate(BaseModel):
    """ORM model for Intermediate"""
    __tablename__ = "Intermediate"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    course_name: Mapped[str]
    type_: Mapped[str] = mapped_column(index=True)
    added: Mapped[Optional[datetime.date]]
    removed: Mapped[Optional[datetime.date]]

    code: Mapped[str]
    competence_type: Mapped[str] = mapped_column(index=True)

    program_name: Mapped[str]
    degree_id: Mapped[int]
    field_code: Mapped[str]
    
    university_id: Mapped[int]
    
    credits: Mapped[int]
    enrollment_year: Mapped[int] = mapped_column(index=True)
    year: Mapped[int] = mapped_column(index=True)