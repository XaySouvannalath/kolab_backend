from typing import Union
from pydantic import BaseModel
from datetime import datetime

class ReviewImage(BaseModel):
    id: Union[int, None] = None
    review_id: int
    filename: str
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
