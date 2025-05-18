from fastapi import APIRouter

router = APIRouter()


# 根据id获取sku
@router.get("/{id}")  # , response_model=SkuBase
async def get_sku_by_id():
    pass
