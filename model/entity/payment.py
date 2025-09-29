from sqlalchemy import  Integer, String, Column
from model.entity.base import Base
from sqlalchemy.orm import relationship


class Payment(Base):
    __tablename__ = "payment"

    id=Column(Integer, primary_key=True)
    person_id = Column(Integer,nullable=False)
    amount = Column(Integer,nullable=False)
    title=Column(String,nullable=False)
    payment_type=Column(String,nullable=False)
    pay_date=Column(String,nullable=False)
    description=Column(String,nullable=False)

    students=relationship("Student", back_populates="payment")
    employees=relationship("Employee", back_populates="payment")

    def __init__(self,person_id:None,amount:object,title:object,payment_type:object,payment_date:object,diecription:object,**kwargs):
        super().__init__(**kwargs)

        self.person_id = person_id
        self.amount = amount
        self.title = title
        self.payment_type = payment_type
        self.payment_date = payment_date
        self.diecription = diecription

    def __repr__(self):
        return f"<Payment(person_id={self.person_id},amount={self.amount}, payment_type={self.payment_type}, title={self.title})>"