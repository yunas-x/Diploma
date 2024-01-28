import datetime
from typing import Optional

from .BaseModel import BaseModel

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Curricula(BaseModel):
    """ORM model for Curricula"""
    __tablename__ = "Curricula"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("Course.id"))
    competence_id: Mapped[int] = mapped_column(ForeignKey("Competence.id"))
    program_id: Mapped[int] = mapped_column(ForeignKey("Program.id"))
    degree_id: Mapped[int] = mapped_column(ForeignKey("Degree.id"))
    field_code: Mapped[int] = mapped_column(ForeignKey("FieldOfStudy.field_code"))
    university_id: Mapped[int] = mapped_column(ForeignKey("University.id"))
    faculty_id: Mapped[int] = mapped_column(ForeignKey("Faculty.id"))
    
    enrollment_year: Mapped[datetime.date] = mapped_column(index=True)
    year: Mapped[int] = mapped_column(index=True)
    credits: Mapped[int]
    classroom_hours: Mapped[Optional[int]]
    
    courses = relationship("Course", back_populates="curriculae")
    competences = relationship("Competence", back_populates="curriculae")
    program = relationship("Program", back_populates="curriculae")
    degree = relationship("Degree", back_populates="curriculae")
    fields_of_study = relationship("FieldOfStudy", back_populates="curriculae")
    university = relationship("University", back_populates="curriculae")
    faculty = relationship("Faculty", back_populates="curriculae")