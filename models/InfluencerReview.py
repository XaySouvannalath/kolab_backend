from typing import Optional
from pydantic import BaseModel
from datetime import datetime, date

class InfluencerReview(BaseModel):
    id: Optional[int]
    influencer_id: int
    brand: Optional[str]
    campaign_name: Optional[str]
    start_at: Optional[date]
    end_at: Optional[date]
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
