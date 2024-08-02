from typing import Optional
from pydantic import BaseModel
from datetime import datetime, date

class FollowerLog(BaseModel):
    id: Optional[int]
    influencer_id: Optional[int]
    platform_id: Optional[int]
    profile_url: Optional[str]
    num_of_follower: Optional[int]
    as_of_date: Optional[date]
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
