from datetime import datetime

from sqlalchemy import Column, Integer, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class PrivateMessage(Base):
    __tablename__ = "private_messages"

    id = Column(Integer, primary_key=True)

    # 对方（无论是用户还是 bot）
    peer_id = Column(Integer, ForeignKey("videos.id"), nullable=False)

    # 是你发的，还是对方发的？
    from_me = Column(Boolean, default=True)

    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    is_read = Column(Boolean, default=False)

    peer = relationship("Video", foreign_keys=[peer_id])
