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