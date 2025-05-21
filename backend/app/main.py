from fastapi import FastAPI
from app.models.base import Base
import uvicorn
from fastapi import APIRouter

from app.models.chatModel import PrivateMessage
from app.models.subtitleModel import Subtitle
from app.models.vedioModel import Video
from app.db import engine
from app.routers.vedioApi import vedio_router


# 创建所有未存在的表
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="SubtitleManager",
    openapi_url="/api/v1/openapi.json",
)
app.include_router(vedio_router, tags=["test"])

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=9999,
        reload=True,
        # log_config="uvicorn_loggin_config.json",
    )
