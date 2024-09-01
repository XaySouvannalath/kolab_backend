from typing import Union
from pydantic import BaseModel
from datetime import datetime

class InfluencerAddress(BaseModel):
    id: Union[int, None] = None
    influencer_id: int
    province_id: Union[int, None] = None
    district_id: Union[int, None] = None
    village_id: Union[int, None] = None
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
