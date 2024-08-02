from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ReviewImage(BaseModel):
    id: Optional[int]
    review_id: int
    image_name: str
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
