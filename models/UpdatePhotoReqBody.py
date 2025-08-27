from typing import Optional, Union
from pydantic import BaseModel

class UpdatePhotoRequestBody(BaseModel):
    influencer_id: Optional[int]
    photo: str