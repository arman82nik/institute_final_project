from sqlalchemy import Column, Integer, String
from model.entity.base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, nullable=False)
    name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    birthday = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)

    def __init__(self, student_id, name, age, gender, birthday, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.birthday = birthday
        self.email = email

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, age={self.age}, gender={self.gender})>"