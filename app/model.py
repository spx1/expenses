from sqlalchemy import Column, String, Date, Integer, Float
from . import db

class CExpense(db.Model):
    __tablename__='Expenses'
    id=Column(Integer, primary_key=True)
    vendor=Column(String(50))
    date=Column(Date)
    amount=Column(Float)



