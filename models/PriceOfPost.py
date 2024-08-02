from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class PriceOfPost(BaseModel):
    id: Optional[int]
    type_of_post_id: int
    influencer_id: int
    price: float
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
