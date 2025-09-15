from sqlalchemy import  Integer, String, Column
from model.entity.base import Base

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer,nullable=False)
    name = Column(String(30),nullable=False)
    age = Column(Integer,nullable=False)
    gender = Column(String(250),nullable=False)
    birthday = Column(String)
    email = Column(String)

    def __init__(self, person_id, name, age, gender, birthday, email):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.birthday = birthday
        self.email = email


    def __repr__(self):
        return f"{self.__dict__}"
