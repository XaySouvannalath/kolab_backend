from typing import Union
from fastapi import APIRouter, HTTPException
from models.Achievement import InfluencerAchievement
from cruds.AchievementService import *

router = APIRouter(
    prefix="/achievement"
)

@router.get("/", tags=["achievement"])
async def get(id: Union[int, None] = None, influencer_id: Union[int, None] = None):
    result = {}
    if id is not None:
        result = await get_achievement(id)
        if result is None:
            raise HTTPException(status_code=404, detail="Achievement not found")
    elif influencer_id is not None:
        result = await get_achievement_by_influencer_id(influencer_id)
        if not result:
            raise HTTPException(status_code=404, detail="No achievements found for this influencer")
    else:
        result = await get_all_achievements()
        if result is None:
            raise HTTPException(status_code=404, detail="Achievement not found")
    return result


@router.post("/", tags=["achievement"])
async def create(achievement: InfluencerAchievement):
    await create_achievement(achievement)
    return achievement


@router.put("/{achievement_id}", response_model=InfluencerAchievement, tags=["achievement"])
async def update(achievement_id: int, achievement: InfluencerAchievement):
    existing_achievement = await get_achievement(achievement_id)
    if existing_achievement is None:
        raise HTTPException(status_code=404, detail="Achievement not found")
    await update_achievement(achievement_id, achievement)
    return achievement


@router.delete("/{achievement_id}", response_model=InfluencerAchievement, tags=["achievement"])
async def delete(achievement_id: int):
    existing_achievement = await get_achievement(achievement_id)
    if existing_achievement is None:
        raise HTTPException(status_code=404, detail="Achievement not found")
    await delete_achievement(achievement_id)
    return existing_achievement
