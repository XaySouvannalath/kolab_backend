from typing import Union
from pydantic import BaseModel
from datetime import datetime

class SocialPlatform(BaseModel):
    id: Union[int, None] = None
    platform_name: Union[str, None]  = None
    is_default: Union[bool, None]  = None
    logo_image: Union[str, None]  = None
    created_date: Union[datetime, None]  = None
    created_by: Union[str, None]  = None
    last_modified_date: Union[datetime, None]  = None
