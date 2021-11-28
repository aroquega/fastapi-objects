from pydantic import BaseModel
from typing import Optional


class ObjectBase(BaseModel):
    name: str
    description: Optional[str]


class Object(ObjectBase):
    id: int

    class Config:
        orm_mode = True


class ObjectCreate(ObjectBase):
    pass
