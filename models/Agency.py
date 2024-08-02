from pydantic import BaseModel
from typing import Optional
from typing import Union

from datetime import datetime

class Agency(BaseModel):
    id: Optional[int]
    agency_name: str
    telephone: Optional[str]
    email: Optional[str]
    address: Optional[str]
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
