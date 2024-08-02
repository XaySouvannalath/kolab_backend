from typing import Union
from fastapi import APIRouter, HTTPException
from models.InfluencerPower import InfluencerPower
from cruds.InfluencerPower import *

router = APIRouter(
    prefix="/influencer_powers"
)

@router.get("/", tags=["influencer_powers"])
async def get(id: Union[str, None] = None):
    result = {}
    if id is not None:
        result = await get_influencer_power(id)
        if result is None:
            raise HTTPException(status_code=404, detail="InfluencerPower not found")
    else:
        result = await get_all_influencer_powers()
        if result is None:
            raise HTTPException(status_code=404, detail="InfluencerPowers not found")
    return result

@router.post("/", tags=["influencer_powers"])
async def create(influencer_power: InfluencerPower):
    await create_influencer_power(influencer_power)
    return influencer_power

@router.put("/{influencer_power_id}", response_model=InfluencerPower, tags=["influencer_powers"])
async def update(influencer_power_id: int, influencer_power: InfluencerPower):
    existing_influencer_power = await get_influencer_power(influencer_power_id)
    if existing_influencer_power is None:
        raise HTTPException(status_code=404, detail="InfluencerPower not found")
    await update_influencer_power(influencer_power_id, influencer_power)
    return influencer_power

@router.delete("/{influencer_power_id}", response_model=InfluencerPower, tags=["influencer_powers"])
async def delete(influencer_power_id: int):
    existing_influencer_power = await get_influencer_power(influencer_power_id)
    if existing_influencer_power is None:
        raise HTTPException(status_code=404, detail="InfluencerPower not found")
    await delete_influencer_power(influencer_power_id)
    return existing_influencer_power


@router.get("/influencer/{influencer_id}", response_model=List[InfluencerPower], tags=["influencer_powers"])
async def get_by_influencer_id(influencer_id: int):
    influencer_powers = await get_influencer_powers_by_influencer_id(influencer_id)
    if not influencer_powers:
        raise HTTPException(status_code=404, detail="No influencer powers found for the given influencer_id")
    return influencer_powers