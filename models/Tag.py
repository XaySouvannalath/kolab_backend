from typing import Optional, Union
from pydantic import BaseModel
from datetime import datetime

class Tag(BaseModel):
    id: Optional[int]
    tag: str
    color: Union[str, None] = None
    description: Optional[str]
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
