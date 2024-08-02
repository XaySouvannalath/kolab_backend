from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Province(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
