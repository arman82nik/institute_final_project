from sqlalchemy import  Integer, String, Column
from model.entity.base import Base



class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer,nullable=False)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    department = Column(String,nullable=False)
    national_id = Column(Integer,nullable=False)
    phone_number = Column(Integer,nullable=False)


    def __init__(self,teacher_id, first_name, last_name, email, department, national_id, phone_number):
        self.id = id
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.department = department
        self.national_id = national_id
        self.phone_number = phone_number

    def __repr__(self):
        return f"{self.__dict__}"