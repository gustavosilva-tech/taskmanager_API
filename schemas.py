from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str] = None
    completed: Optional[bool] = None

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
