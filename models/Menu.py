from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Menu(BaseModel):
    id: Optional[int]
    menu: str
    route: Optional[str]
    description: Optional[str]
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
