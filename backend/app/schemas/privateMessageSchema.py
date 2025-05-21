from datetime import datetime
from pydantic import BaseModel


class PrivateMessageBase(BaseModel):
    sender_id: int
    receiver_id: int
    content: str
    timestamp: datetime = None
    is_read: bool = False


class PrivateMessageCreate(PrivateMessageBase):
    # 创建消息时，可以不传 timestamp，默认由数据库生成
    timestamp: datetime = None


class PrivateMessageRead(PrivateMessageBase):
    id: int

    class Config:
        orm_mode = True  # 允许从ORM模型直接读取数据
