from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class InfluencerRating(BaseModel):
    id: int
    influencer_id: int
    rating_id: int
    category: str
    score: float
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
