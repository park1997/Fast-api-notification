from sqlalchemy import Column, Integer, String, DateTime, func, Enum, Boolean
from sqlalchemy.orm import Session
from app.database import Base

class BaseMixin:
    id = Column(Integer, primary_key = True, index = True)
    created_at = Column(DateTime, nullable = False, default = func.utc_timestamp())
    updated_at = Column(DateTime, nullable = False, default = func.utc_timestamp(), onupdate = func.utc_timestamp())

    def all_columns(self):
        return [c for c in self.__table__.columns if c.primary_key is False and c.name != "created_at"]
    
    def __hash__(self):
        return hash(self,id)
    



