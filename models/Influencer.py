from typing import Optional
from pydantic import BaseModel
from datetime import datetime, date

class Influencer(BaseModel):
    id: Optional[int]
    channel_name: Optional[str]
    content_style: Optional[str]
    is_available: Optional[bool]
    first_name: Optional[str]
    last_name: Optional[str]
    nick_name: Optional[str]
    remark: Optional[str]
    date_of_birth: Optional[date]
    has_agency: Optional[bool]
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
    gender: Optional[str]
