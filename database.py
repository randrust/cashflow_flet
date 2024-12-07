from calendar import c
from sqlalchemy import Boolean, create_engine
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


main_database = "sqlite:///cashflow.db"
engine = create_engine(main_database, echo=True)

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = 'users'
    u_id = Column(Integer, primary_key=True)
    u_username = Column(String)
    u_password = Column(String)
    u_hash_device = Column(String)

class Currencies(Base):
    __tablename__ = 'currencies'
    c_id = Column(Integer, primary_key=True)
    c_name = Column(String)  
    c_short_name = Column(String)
    c_is_main = Column(Boolean)

class CurrencyNominals(Base):
    __tablename__ = 'currency_nominals'
    cn_id = Column(Integer, primary_key=True)
    cn_name = Column(String)
    cn_nominal = Column(Integer)
    cn_currency_id = Column(Integer, ForeignKey('currencies.c_id'))

class CashRecipts(Base):
    __tablename__ = 'cash_recipts'
    cr_id = Column(Integer, primary_key=True)
    cr_date = Column(DateTime)
    cr_currency_nominal_id = Column(Integer, ForeignKey('currency_nominals.cn_id'))
    cr_currency_nominal_amount = Column(Integer)
    cr_user = Column(Integer, ForeignKey('users.u_id'))
    cr_is_synchronized = Column(Boolean)

class InventoryDuration(Base):
    __tablename__ = 'inventory_duration'
    id_id = Column(Integer, primary_key=True)
    id_date_start = Column(DateTime)
    id_date_end = Column(DateTime)

Base.metadata.create_all(bind=engine)

def get_db_data(db_table):
    with Session((engine)) as db:
        data = db.query(db_table).all()
        db.close()
        return data

def database_insert(data):
    with Session((engine)) as db:
        db.add(data)
        db.commit()
        db.refresh(data)
        db.close()

def create_nain_currency_uah():
    main_currency = Currencies(c_name="Гривня", c_short_name="UAH", c_is_main=True)
    database_insert(main_currency)

    main_currency_nominals = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for nominal in main_currency_nominals:
        currency_nominal = CurrencyNominals(cn_name=str(nominal), cn_nominal=nominal, cn_currency_id=main_currency.c_id)
        database_insert(currency_nominal)

def create_administrator():
    user = Users(u_username="admin", u_password="090799", u_hash_device="bnsdfkhgoegnvm,avfnaigfvniog718745094")
    database_insert(user)

def insert_cash_recipt(data):
    cash_recipt = CashRecipts(cr_date=data['cr_date'], cr_currency_nominal_id=data['cr_currency_nominal_id'], cr_currency_nominal_amount=data['cr_currency_nominal_amount'], cr_user=data['cr_user'], cr_is_synchronized=data['cr_is_synchronized'])
    database_insert(cash_recipt)