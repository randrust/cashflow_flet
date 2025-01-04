import datetime
from sqlalchemy import Column, Date, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, Session



main_database = "sqlite:///mainsqlite.db"
engine = create_engine(main_database, echo=True)

class Base(DeclarativeBase):
    pass

class CashFlow(Base):
    __tablename__ = 'cashflow'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    currency1000 = Column(Integer)
    currency500 = Column(Integer)
    currency200 = Column(Integer)
    currency100 = Column(Integer)
    currency50 = Column(Integer)
    Summary = Column(Integer)

Base.metadata.create_all(bind=engine)

def  get_db_data():
    with Session(engine) as session:
        query = session.query(CashFlow).all()
        return query
    

def add_db_data(data):
    with Session(engine) as session:
        session.add(data)
        session.commit()


def delete_db_data(key):
    with Session(engine) as session:
        data = session.query(CashFlow).filter(CashFlow.id == key).first()
        if data is None:
            return
        session.delete(data)
        session.commit()

def update_db_data(data):
    with Session(engine) as session:
        session.add(data)
        session.commit()

# data_ins = CashFlow(date=datetime.date(2023, 1, 2), currency1000=2, currency500=2, currency200=2, currency100=2, currency50=2, Summary=3700)
# add_db_data(data_ins)

data_all = get_db_data()

for data in data_all:
    print(data.id, data.date, data.currency1000, data.currency500, data.currency200, data.currency100, data.currency50, data.Summary)

delete_db_data(4)