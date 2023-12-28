from pydantic import BaseModel
from typing import Optional


class Phonebook(BaseModel):
    surname: str
    name: Optional[str] = None
    base_phone_number: int
    additional_phone_number: Optional[int] = None



