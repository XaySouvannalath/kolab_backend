from typing import List, Union
from pydantic import BaseModel
from datetime import datetime, date
from models.ReviewImage import ReviewImage
class InfluencerReview(BaseModel):
    id: Union[int, None] = None
    influencer_id: int
    brand: Union[str, None] = None
    campaign_name: Union[str, None] = None
    start_at: Union[date, None] = None
    end_at: Union[date, None] = None
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
    score: Union[float, None] = None
    impression: Union[int, None] = None 
    reach: Union[int, None] = None 
    engagement: Union[int, None] = None


class InfluencerReviewResponse(BaseModel):
    id: Union[int, None] = None
    influencer_id: int
    brand: Union[str, None] = None
    campaign_name: Union[str, None] = None
    start_at: Union[date, None] = None
    end_at: Union[date, None] = None
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
    score: Union[float, None] = None
    impression: Union[int, None] = None 
    reach: Union[int, None] = None 
    engagement: Union[int, None] = None
    images: List[ReviewImage]