from typing import Union
from fastapi import APIRouter, HTTPException
from models.Province import Province
from cruds.Province import *

router = APIRouter(
    prefix="/provinces"
)

@router.get("/", tags=["provinces"])
async def get(id: Union[str, None] = None):
    if id is not None:
        result = await get_province(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="Province not found")
    else:
        result = await get_all_provinces()
        if not result:
            raise HTTPException(status_code=404, detail="No provinces found")
    return result

@router.post("/", tags=["provinces"])
async def create(province: Province):
    await create_province(province)
    return province

@router.put("/{province_id}", response_model=Province, tags=["provinces"])
async def update(province_id: int, province: Province):
    existing_province = await get_province(province_id)
    if existing_province is None:
        raise HTTPException(status_code=404, detail="Province not found")
    await update_province(province_id, province)
    return province

@router.delete("/{province_id}", response_model=Province, tags=["provinces"])
async def delete(province_id: int):
    existing_province = await get_province(province_id)
    if existing_province is None:
        raise HTTPException(status_code=404, detail="Province not found")
    await delete_province(province_id)
    return existing_province
