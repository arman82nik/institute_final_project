from sqlalchemy import  Integer, String, Column
from model.entity.base import Base


class Payment(Base):
    __tablename__ = "payment"

    id=Column(Integer, primary_key=True)
    person_id = Column(Integer,nullable=False)
    amount = Column(Integer,nullable=False)
    title=Column(String,nullable=False)
    payment_type=Column(String,nullable=False)
    pay_date=Column(String,nullable=False)
    description=Column(String,nullable=False)


    def __init__(self,person_id,amount,title,payment_type,payment_date,diecription):
        self.person_id = person_id
        self.amount = amount
        self.title = title
        self.payment_type = payment_type
        self.payment_date = payment_date
        self.diecription = diecription

    def __repr__(self):
        return f"{self.__dict__}"