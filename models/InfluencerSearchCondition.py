from typing import List, Optional, Union
from pydantic import BaseModel
from datetime import datetime


class InfluencerSearchCondition(BaseModel):
    id: Union[int, None] = None
    channel_name: Union[str, None] = None
    first_name: Union[str, None] = None
    last_name:  Union[str, None] = None
    province_id: Optional[List[int]] = None  # Optional list of province IDs
    tag_id: Optional[List[int]] = None  # Optional list of tag IDs
    content_style_id: Optional[List[int]] = None  # Optional list of content style IDs
    keyword: Union[str, None] = []
    social_platform_id: Optional[List[int]] = None  # Optional list of content style IDs
    number_of_follower: Union[str, None] = None
    
