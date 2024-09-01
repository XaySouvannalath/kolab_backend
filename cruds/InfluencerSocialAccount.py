from typing import List
from datetime import datetime
from fastapi import HTTPException
from models.InfluencerSocialAccount import InfluencerSocialAccount
from config.database import database

# Assuming you have a Database instance

# CRUD operations
async def create_influencer_social_account(data: InfluencerSocialAccount):
    query = """
    INSERT INTO influencer_social_account (influencer_id, social_platform_id, profile_url, profile_name)
    VALUES (:influencer_id, :social_platform_id, :profile_url, :profile_name)
    """
    values = {
        "influencer_id": data.influencer_id,
        "social_platform_id": data.social_platform_id,
        "profile_url": data.profile_url,
        "profile_name": data.profile_name

    }
    await database.execute(query=query, values=values)
async def update_influencer_social_account(data: InfluencerSocialAccount):
    query = """

    update influencer_social_account set profile_url = :profile_url, profile_name = :profile_name
    where influencer_id = :influencer_id and social_platform_id = :social_platform_id
    """
    values = {
        "influencer_id": data.influencer_id,
        "social_platform_id": data.social_platform_id,
        "profile_url": data.profile_url,
        "profile_name": data.profile_name

    }
    await database.execute(query=query, values=values)

async def get_influencer_social_account(account_id: int):
    query = """
    SELECT id, influencer_id, social_platform_id, profile_url, profile_name, created_date, created_by, last_modified_date
    FROM influencer_social_account
    WHERE id = :id
    """
    account = await database.fetch_one(query=query, values={"id": account_id})
    if not account:
        raise HTTPException(status_code=404, detail="Influencer Social Account not found")
    return account
    
async def get_all_influencer_social_accounts():
    query = """
    SELECT id, influencer_id, social_platform_id, profile_url, profile_name, created_date, created_by, last_modified_date
    FROM influencer_social_account
    """
    accounts = await database.fetch_all(query=query)
    return accounts
# async def get_social_accounts_by_influencer_id(influencer_id: int) -> List[InfluencerSocialAccountResponse]:
# async def get_social_accounts_by_influencer_id(influencer_id: int):
#     query = """
#     SELECT a.*, b.platform_name
#     FROM influencer_social_account a
#     left join social_platform b on b.id = a.social_platform_id
#     WHERE a.influencer_id = :influencer_id
#     """
#     accounts = await database.fetch_all(query=query, values={"influencer_id": influencer_id})
#     if not accounts:
#         raise HTTPException(status_code=404, detail="No social accounts found for this influencer")
#     return accounts
async def get_social_accounts_by_influencer_id(influencer_id: int):
    query = """
        select a.id, a.platform_name, a.logo_image, a.api_follower_link,
        ifnull((select profile_name from influencer_social_account  where influencer_id = :influencer_id and social_platform_id = a.id order by id desc limit 1),"") as profile_name,
        ifnull((select profile_url from influencer_social_account  where influencer_id = :influencer_id and social_platform_id = a.id order by id desc limit 1),"") as profile_url,

        ifnull((select id from influencer_social_account where influencer_id = :influencer_id and social_platform_id = a.id order by id desc limit 1),0) as meta_id,
        ifnull((select num_of_follower from follower_logs where influencer_id  = :influencer_id and platform_id = a.id order by id desc limit 1),0) as num_of_follower
        from social_platform a;

    """
    
    value = {
        "influencer_id": influencer_id,
        "influencer_id": influencer_id,
        "influencer_id": influencer_id,
        "influencer_id": influencer_id,
    }
    
    print(query)
    result = await database.fetch_all(query=query, values=value)
    
    
 
    return result