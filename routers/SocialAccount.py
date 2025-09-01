from typing import Union
from fastapi import APIRouter, HTTPException
from models.RoleMenu import RoleMenu
from cruds.InfluencerSocialAccount import *

router = APIRouter(
    prefix="/SocialAccount"
)

@router.get("/for_insert", tags=["social_account_"])
async def get():
    result = await get_social_accounts_for_insert()
    return result

