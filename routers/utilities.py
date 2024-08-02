
from fastapi import APIRouter, HTTPException
from utilities.social import *

router = APIRouter(
    prefix="/utilities"
)

@router.get("/GetTiktokFollower", tags=["utilities"])
async def get_tiktok_follower(username):
    return get_tiktok_followers(username)

@router.get("/GetFacebookFollower", tags=["utilities"])
async def get_facebook_follower(username):
    return get_facebook_followers(username)


