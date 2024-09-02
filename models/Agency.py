from pydantic import BaseModel
from typing import Optional
from typing import Union

from datetime import datetime

 

class Agency(BaseModel):
    id: Union[int, None]
    agency_name: str
    telephone: Union[str, None]
    email: Union[str, None]
    address: Union[str, None]
    created_date: Union[datetime, None]
    created_by: Union[str, None]
    last_modified_date: Union[datetime, None]


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
