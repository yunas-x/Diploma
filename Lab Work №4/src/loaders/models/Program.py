from .BaseModel import BaseModel

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Program(BaseModel):
    """ORM model for Program"""
    __tablename__ = "Program"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    program_name: Mapped[str]
    
    curriculae = relationship("Curricula", back_populates="program")