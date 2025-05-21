from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class VideoSchema(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., max_length=255)
    file_path: str
    duration: Optional[float] = None
    language: Optional[str] = Field(None, max_length=10)
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
