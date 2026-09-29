from pydantic import BaseModel
from typing import Optional

class HabitBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: Optional[bool] = True

class HabitCreate(HabitBase):
    pass

class Habit(HabitBase):
    id: int

    class Config:
        from_attributes = True