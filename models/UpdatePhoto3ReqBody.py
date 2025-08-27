from typing import Optional, Union
from pydantic import BaseModel

class UpdatePhoto3RequestBody(BaseModel):
    influencer_id: Optional[int]
    photo3: str