from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class SocialPlatform(BaseModel):
    id: Optional[int]
    platform_name: Optional[str]
    is_default: Optional[bool]
    logo_image: Optional[str]
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
