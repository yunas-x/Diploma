from datetime import datetime
from pydantic import BaseModel

class ApiSession(BaseModel):
    session_id: str
    created_at: datetime