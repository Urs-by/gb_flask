from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str
    surname: str
    age: int
    gender: str
    group: str
