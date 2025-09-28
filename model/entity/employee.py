from sqlalchemy import  Integer, String, Column
from model.entity.base import Base
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    national_id = Column(String,nullable=False)
    birthday = Column(String,nullable=False)
    email = Column(String,nullable=False)
    job_title = Column(String,nullable=False)
    department = Column(String,nullable=False)
    hire_date = Column(String,nullable=False)
    salary = Column(String,nullable=False)

    registers=relationship("Register", back_populates="employee")
    payments = relationship("Payment", back_populates="employee")


    def __init__(self, first_name:object,last_name:object,national_id:None,birthday:object,email:object,job_title:object,department:object,hire_date:object,salary:object,**kwargs):
        super().__init__(**kwargs)

        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.birthday = birthday
        self.email = email
        self.job_title = job_title
        self.department = department
        self.hire_date = hire_date
        self.salary = salary

    def __repr__(self):
        return f"<employee(national_id={self.national_id},first_name={self.first_name}, last_name={self.last_name}, department={self.department})>"

