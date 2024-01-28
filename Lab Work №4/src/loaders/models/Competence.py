import enum
from .BaseModel import BaseModel

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class CompetenceType(enum.Enum):
    UNIVERSAL = "УК"
    GENERAL_PROFESSIONAL = "ОПК"
    PROFESSIONAL = "ПК"

class Competence(BaseModel):
    """ORM model for Competence"""
    __tablename__ = "Competence"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    code: Mapped[str]
    competence_type: Mapped[CompetenceType] = mapped_column(index=True)
    name: Mapped[str]
    
    curriculae = relationship("Curricula", back_populates="competences")