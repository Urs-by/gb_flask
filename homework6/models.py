from pydantic import BaseModel, Field


class TaskIn(BaseModel):
    title: str = Field(title="title", max_length=50)
    description: str = Field(title="Description", max_length=150)
    done: bool=Field(title="Done", default=False)

class TaskOut(TaskIn):
    id: int