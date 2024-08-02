from typing import Union
from fastapi import APIRouter, HTTPException
from models.SocialPlatform import SocialPlatform
from cruds.SocialPlatform import *

router = APIRouter(
    prefix="/social_platforms"
)

@router.get("/", tags=["social_platforms"])
async def get(id: Union[int, None] = None):
    if id is not None:
        result = await get_social_platform(id)
        if result is None:
            raise HTTPException(status_code=404, detail="Social platform not found")
    else:
        result = await get_all_social_platforms()
        if not result:
            raise HTTPException(status_code=404, detail="No social platforms found")
    return result

@router.post("/", tags=["social_platforms"])
async def create(platform: SocialPlatform):
    await create_social_platform(platform)
    return platform

@router.put("/{platform_id}", response_model=SocialPlatform, tags=["social_platforms"])
async def update(platform_id: int, platform: SocialPlatform):
    existing_platform = await get_social_platform(platform_id)
    if existing_platform is None:
        raise HTTPException(status_code=404, detail="Social platform not found")
    await update_social_platform(platform_id, platform)
    return platform

@router.delete("/{platform_id}", response_model=SocialPlatform, tags=["social_platforms"])
async def delete(platform_id: int):
    existing_platform = await get_social_platform(platform_id)
    if existing_platform is None:
        raise HTTPException(status_code=404, detail="Social platform not found")
    await delete_social_platform(platform_id)
    return existing_platform
