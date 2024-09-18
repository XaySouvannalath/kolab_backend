

from typing import Union
from pydantic import BaseModel
from datetime import datetime, date

class LoginModel(BaseModel):    
    username: Union[str, None] = None 
    password: Union[str, None] = None
