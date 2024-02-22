from sqlalchemy import DateTime, ForeignKey, func
from .BaseModel import BaseModel

from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Token(BaseModel):
    """ORM model for Token"""
    __tablename__ = "Token"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    token: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), index=True)
    posted_on: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                server_default=func.now())
    
    user = relationship("User", back_populates="tokens")