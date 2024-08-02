from typing import Union
from fastapi import APIRouter, HTTPException
from models.Influencer import Influencer
from cruds.influencer import *

router = APIRouter(
    prefix="/influencer"
)

@router.get("/", tags=["influencer"])
async def get(id: Union[str, None] = None):
    result = {}
    if id is not None:
        result = await get_influencer(id)
        if result is None:
            raise HTTPException(status_code=404, detail="Influencer not found")
    else:
        result = await get_all_influencers()
        if result is None:
            raise HTTPException(status_code=404, detail="Influencers not found")
    return result

@router.post("/", tags=["influencer"])
async def create(influencer: Influencer):
    await create_influencer(influencer)
    return influencer

@router.put("/{influencer_id}", response_model=Influencer, tags=["influencer"])
async def update(influencer_id: int, influencer: Influencer):
    existing_influencer = await get_influencer(influencer_id)
    if existing_influencer is None:
        raise HTTPException(status_code=404, detail="Influencer not found")
    await update_influencer(influencer_id, influencer)
    return influencer

@router.delete("/{influencer_id}", response_model=Influencer, tags=["influencer"])
async def delete(influencer_id: int):
    existing_influencer = await get_influencer(influencer_id)
    if existing_influencer is None:
        raise HTTPException(status_code=404, detail="Influencer not found")
    await delete_influencer(influencer_id)
    return existing_influencer
