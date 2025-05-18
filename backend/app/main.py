from fastapi import FastAPI
from app.models.base import Base

# from app.models.chatModel import PrivateMessage
from app.models.subtitleModel import Subtitle
from app.models.vedioModel import Video
from app.db import engine
import uvicorn

# 创建所有未存在的表
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="SubtitleManager",
    openapi_url="/api/v1/openapi.json",
)


# 示例路由（可选）
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=9999,
        reload=True,
        # log_config="uvicorn_loggin_config.json",
    )
