from sqlalchemy.orm import Mapped
from .BaseModel import BaseModel
from sqlalchemy.orm import mapped_column

class MVP_API(BaseModel):
    """ORM model for mvp_api"""
    __tablename__ = "mvp_api"

    program_id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    program_name: Mapped[str]
    degree_id: Mapped[int]
    field_code: Mapped[str]
