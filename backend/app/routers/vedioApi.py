from fastapi import APIRouter

vedio_router = APIRouter()


### 直接写业务逻辑，然后给main函数调用,力求简单，快速开始flutter
# 根据id获取sku
@vedio_router.get("/{id}")  # , response_model=SkuBase
async def get_sku_by_id():
    return 1
