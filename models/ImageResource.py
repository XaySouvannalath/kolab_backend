from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ImageResource(BaseModel):
    id: Optional[int]
    image_name: Optional[str]
    original_name: Optional[str]
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
