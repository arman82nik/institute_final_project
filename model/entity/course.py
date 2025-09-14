from sqlalchemy import Column, Integer, String, Date,Time
from model.entity.base import Base

class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String(30),nullable=False)
    teacher = Column(String(30),nullable=False)
    start_date = Column(Date,nullable=False)
    end_date = Column(Date,nullable=False)
    start_time = Column(Time,nullable=False)
    end_time = Column(Time,nullable=False)
    type_class=Column("type_class",String(10),nullable=False)


    def __init__(self, name: object, teacher: object, start_date: object, end_date: object, start_time: object, end_time: object, type_class: object) -> None:
        self.name = name
        self.teacher = teacher
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.type_class = type_class
        
    def __repr__(self):
        return f"<Course(name={self.name}, teacher={self.teacher}, type={self.type_class})>"




