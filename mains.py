from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase



main_database = "sqlite:///mainsqlite.db"
engine = create_engine(main_database, echo=True)

class Base(DeclarativeBase):
    pass

class CashFlow(Base):
    __tablename__ = 'cashflow'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    currency1000 = Column(Integer)
    currency500 = Column(Integer)
    currency200 = Column(Integer)
    currency100 = Column(Integer)
    currency50 = Column(Integer)
    Summary = Column(Integer)