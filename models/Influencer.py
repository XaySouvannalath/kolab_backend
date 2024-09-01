from typing import List, Union
from pydantic import BaseModel
from datetime import datetime, date
from models.InfluencerSocialAccount import InfluencerSocialAccount
from models.InfluencerTagResponse import InfluencerTagModel

class Influencer(BaseModel):
    id: Union[int, None] = None
    channel_name: Union[str, None] = None
    content_style_id: Union[int, None] = None
    content_style: Union[str,None] = None
    is_available: Union[bool, None] = None
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    nick_name: Union[str, None] = None
    remark: Union[str, None] = None
    date_of_birth: Union[date, None] = None
    has_agency: Union[bool, None] = None
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
    gender: Union[str, None] = None
    agency_id: Union[int, None] = None
    photo: Union[str, None] = None
    province_id: Union[int, None] = None
    province_description: Union[str, None] = None
    tags: List[InfluencerTagModel] = None
    agency_name: Union[str, None] = None
    birth_place: Union[int, None] = None
    birth_place_description: Union[str, None] = None
    impression: Union[int, None] = None 
    reach: Union[int, None] = None 
    engagement: Union[int, None] = None
    social_accounts: List[InfluencerSocialAccount] = None
    
