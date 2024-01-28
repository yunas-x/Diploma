from .BaseModel import BaseModel

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Faculty(BaseModel):
    """ORM model for Faculty"""
    __tablename__ = "Faculty"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    
    curriculae = relationship("Curricula", back_populates="faculty")