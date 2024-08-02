from typing import Union
from fastapi import APIRouter, HTTPException
from models.InfluencerAddress import InfluencerAddress
from cruds.InfluencerAddress import *

router = APIRouter(
    prefix="/influencer_addresses"
)

@router.get("/", tags=["influencer_addresses"])
async def get(id: Union[str, None] = None):
    result = {}
    if id is not None:
        result = await get_influencer_address(id)
        if result is None:
            raise HTTPException(status_code=404, detail="InfluencerAddress not found")
    else:
        result = await get_all_influencer_addresses()
        if result is None:
            raise HTTPException(status_code=404, detail="InfluencerAddresses not found")
    return result

@router.post("/", tags=["influencer_addresses"])
async def create(influencer_address: InfluencerAddress):
    await create_influencer_address(influencer_address)
    return influencer_address

@router.put("/{influencer_address_id}", response_model=InfluencerAddress, tags=["influencer_addresses"])
async def update(influencer_address_id: int, influencer_address: InfluencerAddress):
    existing_influencer_address = await get_influencer_address(influencer_address_id)
    if existing_influencer_address is None:
        raise HTTPException(status_code=404, detail="InfluencerAddress not found")
    await update_influencer_address(influencer_address_id, influencer_address)
    return influencer_address

@router.delete("/{influencer_address_id}", response_model=InfluencerAddress, tags=["influencer_addresses"])
async def delete(influencer_address_id: int):
    existing_influencer_address = await get_influencer_address(influencer_address_id)
    if existing_influencer_address is None:
        raise HTTPException(status_code=404, detail="InfluencerAddress not found")
    await delete_influencer_address(influencer_address_id)
    return existing_influencer_address
