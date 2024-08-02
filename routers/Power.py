from typing import Union
from fastapi import APIRouter, HTTPException
from models.Power import Power
from cruds.Power import *

router = APIRouter(
    prefix="/powers"
)

@router.get("/", tags=["powers"])
async def get(id: Union[str, None] = None):
    result = {}
    if id is not None:
        result = await get_power(id)
        if result is None:
            raise HTTPException(status_code=404, detail="Power not found")
    else:
        result = await get_all_powers()
        if result is None:
            raise HTTPException(status_code=404, detail="Powers not found")
    return result

@router.post("/", tags=["powers"])
async def create(power: Power):
    await create_power(power)
    return power

@router.put("/{power_id}", response_model=Power, tags=["powers"])
async def update(power_id: int, power: Power):
    existing_power = await get_power(power_id)
    if existing_power is None:
        raise HTTPException(status_code=404, detail="Power not found")
    await update_power(power_id, power)
    return power

@router.delete("/{power_id}", response_model=Power, tags=["powers"])
async def delete(power_id: int):
    existing_power = await get_power(power_id)
    if existing_power is None:
        raise HTTPException(status_code=404, detail="Power not found")
    await delete_power(power_id)
    return existing_power
