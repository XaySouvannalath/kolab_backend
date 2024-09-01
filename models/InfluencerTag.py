from typing import Union
from pydantic import BaseModel
from datetime import datetime

class InfluencerTag(BaseModel):
    id: Union[int, None] = None
    influencer_id: int
    tag_id: int
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
    
    #from inner join
    tag:  Union[str, None] = None
    channel_name:  Union[str, None] = None
