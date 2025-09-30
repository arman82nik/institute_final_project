from sqlalchemy import  Integer, String, Column
from model.entity.base import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer,nullable=False)
    name = Column(String(30),nullable=False)
    age = Column(Integer,nullable=False)
    gender = Column(String(250),nullable=False)
    birthday = Column(String,nullable=False)
    email = Column(String,nullable=False)

    def __init__(self, student_id:None, name:object, age:object, gender:object, birthday:object, email:object,**kwargs):
        super().__init__(**kwargs)
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.birthday = birthday
        self.email = email



    def __repr__(self):
        return f"<Student(student_id={self.student_id},name={self.name}, age={self.age}, gender={self.gender})>"
