from sqlalchemy import DateTime, ForeignKey, func
from .BaseModel import BaseModel

from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Report(BaseModel):
    """ORM model for Report"""
    __tablename__ = "Report"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), index=True)
    text: Mapped[str]
    posted_on: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                server_default=func.now())
    
    user = relationship("User", back_populates="reports")