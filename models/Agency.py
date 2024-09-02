from pydantic import BaseModel
from typing import Optional
from typing import Union

from datetime import datetime

 

class Agency(BaseModel):
    id: Union[int, None] = None
    agency_name: str
    telephone: Union[str, None]
    email: Union[str, None]
    address: Union[str, None]
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
