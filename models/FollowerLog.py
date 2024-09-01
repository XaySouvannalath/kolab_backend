from typing import Union
from pydantic import BaseModel
from datetime import datetime, date

class FollowerLog(BaseModel):
    id: Union[int, None] = None
    influencer_id: Union[int, None] = None
    platform_id: Union[int, None] = None
    profile_url: Union[str, None] = None
    num_of_follower: Union[int, None] = None
    as_of_date: Union[date, None] = None
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
