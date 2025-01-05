import flet as ft
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
        data = session.get(CashFlow, key)
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

# data_all = get_db_data()

# for data in data_all:
#     # print(data.id, data.date, data.currency1000, data.currency500, data.currency200, data.currency100, data.currency50, data.Summary)
#     print(data.__dict__)

# delete_db_data(5)
        
def main(page: ft.Page):
    page.title = "Cash Flow"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    date_from = ft.ElevatedButton(text=datetime.date.today().strftime("%Y-%m-%d"), on_click=lambda e: page.open(
                ft.DatePicker(first_date=datetime.datetime(year=2025, month=1, day=1),
                    last_date=datetime.datetime(year=2025, month=12, day=31),)))
    date_to = ft.ElevatedButton(text=datetime.date.today().strftime("%Y-%m-%d"), on_click=lambda e: page.open(
                ft.DatePicker(first_date=datetime.datetime(year=2025, month=1, day=1),
                    last_date=datetime.datetime(year=2025, month=12, day=31),)))
    
    
    
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Date")),
            ft.DataColumn(ft.Text("Summary")),
        ],
        rows=[],
    )

    data_all = get_db_data()
    for data in data_all:
        data_table.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(data.id)),
                ft.DataCell(ft.Text(data.date)),
                ft.DataCell(ft.Text(data.Summary)),
            ]))


    page.add(
        ft.Row(
            [
                date_from,
                ft.Text(" <---> "),
                date_to,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [data_table,],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

ft.app(main)