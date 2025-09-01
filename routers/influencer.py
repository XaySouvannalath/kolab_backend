from typing import Union
from fastapi import APIRouter, HTTPException
from models.Influencer import Influencer
from cruds.influencer import *
from models.InfluencerSearchCondition import InfluencerSearchCondition
from fastapi import Depends
from cruds.AchievementService import *
from models.UpdatePhoto2ReqBody import UpdatePhoto2RequestBody
from models.UpdatePhoto3ReqBody import  UpdatePhoto3RequestBody
from models.UpdatePhotoReqBody import UpdatePhotoRequestBody
from utilities.DateManipulation import lao_date_to_iso

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


@router.post("/search", tags=["influencer"])
# async def search(conditions: InfluencerSearchCondition = Depends()):
async def search(conditions: InfluencerSearchCondition):
    result = {}
    result = await search_influencer(conditions=conditions)
    if result is None:
            raise HTTPException(status_code=404, detail="Influencers not found")
    return result

    

@router.post("/", tags=["influencer"])
async def create(influencer: Influencer):
    # save influencer
    influencer.date_of_birth = lao_date_to_iso(influencer.date_of_birth)
    new_id = await create_influencer(influencer)

    # save social account
    social_accounts = influencer.social_accounts
    for social_account in social_accounts:
        social_account.influencer_id = new_id
        await create_influencer_social_account(social_account)


    #insert achievement
    achievements = influencer.achievements
    for achievement in achievements:
        if achievement.id is None:
            await create_achievement(achievement)
    return influencer

@router.put("/{influencer_id}",  tags=["influencer"])
async def update(influencer_id: int, influencer: Influencer):
    
    print("UPDATE INFLUENCER")

    influencer.date_of_birth = lao_date_to_iso(influencer.date_of_birth)
    existing_influencer = await get_influencer(influencer_id)
    if existing_influencer is None:
        raise HTTPException(status_code=404, detail="Influencer not found")

    #update influ

    #update social account
    social_accounts = influencer.social_accounts
    for social_account in social_accounts:
        print("AVERAGE_ENGAGEMENT ", social_account.average_engagement)
        await update_influencer_social_account(social_account)


    #update achievement
    achievements = influencer.achievements
    for achievement in achievements:
        if achievement.id is None:
            await create_achievement(achievement)

    await update_influencer(influencer_id, influencer)
    return influencer

@router.delete("/{influencer_id}", response_model=Influencer, tags=["influencer"])
async def delete(influencer_id: int):
    existing_influencer = await get_influencer(influencer_id)
    if existing_influencer is None:
        raise HTTPException(status_code=404, detail="Influencer not found")
    await delete_influencer(influencer_id)
    return existing_influencer

@router.post("/update_influencer_photo", tags=["influencer"])
async def updateInfluencerPhoto(updatePhoto: UpdatePhotoRequestBody):
    await update_influencer_photo(updatePhoto.influencer_id, updatePhoto.photo)
    return updatePhoto

@router.post("/update_influencer_photo2", tags=["influencer"])
async def updateInfluencerPhoto(updatePhoto: UpdatePhoto2RequestBody):
    await update_influencer_photo2(updatePhoto.influencer_id, updatePhoto.photo2)
    return updatePhoto

@router.post("/influencer/update_influencer_photo3", tags=["influencer"])
async def updateInfluencerPhoto(updatePhoto: UpdatePhoto3RequestBody):
    await update_influencer_photo3(updatePhoto.influencer_id, updatePhoto.photo3)
    return updatePhoto

