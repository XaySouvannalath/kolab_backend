from fastapi import APIRouter, Depends, HTTPException
from typing import List, Union
from models.InfluencerSocialAccount import InfluencerSocialAccount
from cruds.InfluencerSocialAccount import *
from cruds.FollowerLog import *
router = APIRouter(
    prefix="/social-account"
)

@router.post("/",tags=["Influencer Social Account"])
async def create_account(data: InfluencerSocialAccount):
    account_id = await create_influencer_social_account(data)
    return await get_influencer_social_account(account_id)

# @router.get("/{account_id}", tags=["Influencer Social Account"])
# async def get_account(account_id: int):
#     return await get_influencer_social_account(account_id)

@router.get("/", tags=["Influencer Social Account"])
async def get_all_accounts():
    return await get_all_influencer_social_accounts()

@router.get("/by_influencer_id", tags=["Influencer Social Account"])
async def get_by_influencer(influencer_id: int):
    response = []
    if influencer_id is not None:
        result = await get_social_accounts_by_influencer_id(influencer_id)
        if result is None:
            raise HTTPException(status_code=404, detail="not found")
    for r in result:
        # print(r["influencer_id"])
        response.append(InfluencerSocialAccount(
            id=r["id"],
            # influencer_id=r["influencer_id"],
            # social_platform_id=r["social_platform_id"],
            profile_url=r["profile_url"],
            profile_name=r["profile_name"],
            logo_image=r["logo_image"],
            meta_id=r["meta_id"],
            api_follower_link=r["api_follower_link"],
            num_of_follower=r["num_of_follower"],
            platform_name=r["platform_name"]
        ))
        
    #    id,
    #    platform_name
    #    logo_name,
    #    api_follower_link,
    #    profile_name,
    #    meta_id
    #    num_of_follower
        
        # response.append(
        #     InfluencerSocialAccount(
        #         id=r["id"],
                # influencer_id=r["influencer_id"],
        #         social_platform_id=r["social_platform_id"],
        #         profile_url=r["profile_url"],
        #         profile_name=r["profile_name"],
        #         meta_id=r["meta_id"],
        #         api_follower_link=r["api_follower_link"],
        #         num_of_follower=r["num_of_follower"]
        #     )
        # )
    return response

@router.post("/save_social_account_list", tags=["Influencer Social Account"])
async def save_price_list(influencer_id: int, social_list: List[InfluencerSocialAccount]):

    for pl in social_list:
        pl.influencer_id = influencer_id
        if pl.meta_id == 0:
            # insert
            print("saving")
            await create_influencer_social_account(
                     pl
            )
            
            # save follower logs
            await create_follower_log(
                FollowerLog(
                    influencer_id=influencer_id,
                    platform_id=pl.social_platform_id,
                    num_of_follower=pl.num_of_follower
                )
            )
            
        else:
            #update
            print("updating")
            await update_influencer_social_account(
                pl
            )
            
            # save follower logs
            print("social platform id")
             
            
            await create_follower_log(
                FollowerLog(
                    influencer_id=influencer_id,
                    platform_id=pl.social_platform_id,
                    num_of_follower=pl.num_of_follower
                )
            )
            
    return social_list
                