# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite 本地数据库路径（可改成你想要的位置）
SQLALCHEMY_DATABASE_URL = "sqlite:///./spotv.db"

# 创建 Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 创建 SessionLocal 类（之后用它来创建 session）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
