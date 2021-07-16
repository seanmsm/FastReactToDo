from pydantic import BaseModel
from typing import List


class TaskDataModel(BaseModel):
    desc: str
    tags: List[str]
    completed: bool


class TaskModel(BaseModel):
    id: int
    desc: str
    tags: List[str]
    completed: bool