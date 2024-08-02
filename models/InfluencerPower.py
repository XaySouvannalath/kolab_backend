from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class RateEnum(str, Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class InfluencerPower(BaseModel):
    id: Optional[int]
    influencer_id: int
    power_id: int
    amount: Optional[float]
    rate: Optional[RateEnum]
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
