from pydantic import BaseModel
from typing import List

class user(BaseModel):
    userId: str
    password: str
