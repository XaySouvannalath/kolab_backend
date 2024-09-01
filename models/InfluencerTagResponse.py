from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class InfluencerTagModel(BaseModel):
    influencer_tag_id: int
    tag: str
    color: str

class InfluencerTagsResponse(BaseModel):
    channel_name: str
    tags: List[InfluencerTagModel]

   