from typing import Union
from pydantic import BaseModel
from datetime import datetime

class PriceOfPost(BaseModel):
    id: Union[int, None] = None
    type_of_post_id: int
    influencer_id: int
    price: float
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None



class PriceOfPostOfInfluencer(BaseModel):
    id: Union[int, None] = None
    name: Union[str, None] =None
    description: Union[str, None] = None
    price: Union[float, None] = None
    meta_id: Union[int, None] = None