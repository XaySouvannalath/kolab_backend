from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ReviewInsight(BaseModel):
    id: Optional[int]
    review_id: int
    power_id: int
    amount: Optional[float]
    rate: Optional[str]  # Enum values as string
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
