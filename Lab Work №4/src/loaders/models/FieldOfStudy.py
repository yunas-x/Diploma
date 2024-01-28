from typing import Optional
from .BaseModel import BaseModel

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class FieldOfStudy(BaseModel):
    """ORM model for FieldOfStudy"""
    __tablename__ = "FieldOfStudy"
    
    field_code: Mapped[str] = mapped_column(primary_key=True, index=True, autoincrement=False)
    field_group_code: Mapped[Optional[str]] = mapped_column(ForeignKey("FieldOfStudy.field_code"), index=True)
    field_name: Mapped[str] = mapped_column(index=True)
    
    children_fields = relationship("FieldOfStudy", back_populates="parent_group")
    parent_group = relationship("FieldOfStudy", back_populates="children_fields", remote_side=[field_code])

    curriculae = relationship("Curricula", back_populates="fields_of_study")