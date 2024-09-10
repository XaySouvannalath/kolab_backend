
from fastapi import APIRouter, HTTPException
from utilities.social import *
from utilities.apify import *

router = APIRouter(
    prefix="/utilities"
)

@router.get("/GetTiktokFollower", tags=["utilities"])
async def get_tiktok_follower(username):
    return get_tiktok_followers(username)

@router.get("/GetFacebookFollower", tags=["utilities"])
async def get_facebook_follower(username):
    return get_facebook_followers(username)


@router.get("/GetFacebookTimeline", tags=["utilities"])
async def get_facebook_timeline():
    return get_fb_user_timeline()


@router.get("/GetYoutubeFollower", tags=["utilities"])
async def get_youtube_follower(username):
    return get_youtube_followers(username=username)


@router.get("/InfluencerDataLastUpdateTime", tags=["utilities"])
async def getInfluencerDataLastUpdateTime(influencer_id: int):
    # return "okk"
    return get_influencer_data_last_update_time(influencer_id=influencer_id)