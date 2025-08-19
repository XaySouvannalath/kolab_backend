from pydantic import BaseModel
from typing import Union
from datetime import datetime

class InfluencerAchievement(BaseModel):
    id: Union[int, None] = None
    influencer_id: int
    achievement_text: Union[str, None] = None
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
