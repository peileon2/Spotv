from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SubtitleSchema(BaseModel):
    id: Optional[int] = None
    video_id: int
    language: str = Field(..., max_length=10)
    start_time: float
    end_time: float
    content: str = Field(..., max_length=250)
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
