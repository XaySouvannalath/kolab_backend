from typing import Union
from pydantic import BaseModel
from datetime import datetime

# Pydantic model for request and response
class InfluencerSocialAccount(BaseModel):
    id: int
    influencer_id: Union[int, None] = None
    social_platform_id: Union[int, None] = None
    profile_url: Union[str, None] = None
    profile_name: Union[str, None] = None
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
    meta_id: Union[int, None] = None
    api_follower_link: Union[str, None] = None
    num_of_follower: Union[int,None]= None
    
    # extra
    platform_name: Union[str, None] = None
    logo_image: Union[str,None] = None


