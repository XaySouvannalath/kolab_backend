from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class AgencyInfluencer(BaseModel):
    id: Optional[int]
    agency_id: int
    influencer_id: int
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
