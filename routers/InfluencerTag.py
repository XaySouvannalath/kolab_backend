from typing import Union
from fastapi import APIRouter, HTTPException
from models.InfluencerTag import InfluencerTag
from cruds.InfluencerTag import *

router = APIRouter(
    prefix="/influencer_tags"
)

@router.get("/", tags=["influencer_tags"])
async def get(id: Union[str, None] = None):
    if id is not None:
        result = await get_influencer_tag(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="InfluencerTag not found")
    else:
        result = await get_all_influencer_tags()
        if not result:
            raise HTTPException(status_code=404, detail="No InfluencerTags found")
    return result
@router.get("/v2", tags=["influencer_tags"])
async def get_v2(id: Union[str, None] = None):
    if id is not None:
        result = await get_influencer_tags_v2(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="InfluencerTag not found")
    else:
        result = await get_influencer_tags_v2()
        if not result:
            raise HTTPException(status_code=404, detail="No InfluencerTags found")
    return result

@router.post("/", tags=["influencer_tags"])
async def create(influencer_tag: InfluencerTag):
    await create_influencer_tag(influencer_tag)
    return influencer_tag

@router.put("/{tag_id}", response_model=InfluencerTag, tags=["influencer_tags"])
async def update(tag_id: int, influencer_tag: InfluencerTag):
    existing_tag = await get_influencer_tag(tag_id)
    if existing_tag is None:
        raise HTTPException(status_code=404, detail="InfluencerTag not found")
    await update_influencer_tag(tag_id, influencer_tag)
    return influencer_tag

@router.delete("/{tag_id}", response_model=InfluencerTag, tags=["influencer_tags"])
async def delete(tag_id: int):
    existing_tag = await get_influencer_tag(tag_id)
    if existing_tag is None:
        raise HTTPException(status_code=404, detail="InfluencerTag not found")
    await delete_influencer_tag(tag_id)
    return existing_tag
