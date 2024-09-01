from typing import Optional, Union
from pydantic import BaseModel
from datetime import datetime

class ContentStyle(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Union[str, None] = None
    created_date:  Union[datetime, None] = None
    created_by:  Union[str, None] = None
    last_modified_date:  Union[datetime, None] = None
