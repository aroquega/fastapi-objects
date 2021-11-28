from database import Base
from sqlalchemy import Column, Integer, String


class Object(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
