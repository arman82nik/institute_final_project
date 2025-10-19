from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base



class Classroom(Base):
    __tablename__ = 'classroom'
    id = Column(Integer, primary_key=True)
    class_number = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    course = Column(String(30),nullable=False)
    teacher = Column(String(30),nullable=False)

    registers = relationship("register", back_populates="classroom")
    projects = relationship("Project", back_populates="classroom")


    def __init__(self, class_number:object,floor:object,
                 start_time:object,end_time:object,
                 course:object,teacher:object, **kwargs):
        super().__init__(**kwargs)
        self.class_number = class_number
        self.floor = floor
        self.start_time = start_time
        self.end_time = end_time
        self.course = course
        self.teacher = teacher


    def __repr__(self):
        return f"<classroom({self.class_number}, {self.floor}, {self.course}, {self.teacher})>"
