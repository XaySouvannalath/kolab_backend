from typing import Union
from pydantic import BaseModel
from datetime import datetime

class ImageResource(BaseModel):
    id: Union[int, None] = None
    image_name: Union[str, None] = None
    original_name: Union[str, None] = None
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
