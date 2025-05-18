from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Boolean,
    Float,
    ForeignKey,
)
from app.models.base import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)  # 视频标题
    file_path = Column(String, nullable=False)  # 视频文件路径（可选）
    duration = Column(Float, nullable=True)  # 视频总时长（秒）
    language = Column(String(10), nullable=True)  # 原始语言
    created_at = Column(DateTime, default=datetime.utcnow)
