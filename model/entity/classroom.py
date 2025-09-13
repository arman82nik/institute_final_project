from sqlalchemy import Column, Integer, String, DateTime ,Time
from model.entity.base import Base

class Classroom(Base):
    __tablename__ = 'classroom'

    id = Column(Integer, primary_key=True)
    name = Column(String(30),nullable=False)
    teacher = Column(String(30),nullable=False)
    start_date = Column(DateTime,nullable=False)
    end_date = Column(DateTime,nullable=False)
    start_time = Column(Time,nullable=False)
    end_time = Column(Time,nullable=False)
    type_class=Column(String(10),nullable=False)


    def __init__(self, name, teacher, start_date, end_date, start_time, end_time, type_class):
        self.name = name
        self.teacher = teacher
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.type_class = type_class





