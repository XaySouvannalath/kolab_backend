from typing import Union
from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
    id: Union[int, None] = None
    name: str
    description: Union[str, None] = None
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None

