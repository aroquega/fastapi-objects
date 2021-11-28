from pydantic import BaseModel
from typing import Optional


class ObjectBase(BaseModel):
    name: str
    description: Optional[str]


class Object(BaseModel):
    class Config:
        orm_mode = True


class ObjectCreate(ObjectBase):
    pass

