from typing import Union
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class RateEnum(str, Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class InfluencerPower(BaseModel):
    id: Union[int, None] = None
    influencer_id: int
    power_id: int
    amount: Union[float, None] = None
    rate: Union[RateEnum, None] = None
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
