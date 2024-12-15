from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Currencies(Base):
    __tablename__ = 'currencies'
    c_id = Column(Integer, primary_key=True)
    c_name = Column(String)
    c_short_name = Column(String)
    c_is_main = Column(Boolean)