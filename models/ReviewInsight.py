from typing import Union
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class RateEnum(str, Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class ReviewInsight(BaseModel):
    id: Union[int, None] = None
    review_id: int
    power_id: int
    amount: Union[float, None] = None
    rate: Union[RateEnum, None] = None  # Use the Enum for the rate
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
