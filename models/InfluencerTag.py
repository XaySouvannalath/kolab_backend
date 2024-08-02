from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class InfluencerTag(BaseModel):
    id: Optional[int]
    influencer_id: int
    tag_id: int
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
