from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class InfluencerAddress(BaseModel):
    id: Optional[int]
    influencer_id: int
    province_id: Optional[int]
    district_id: Optional[int]
    village_id: Optional[int]
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
