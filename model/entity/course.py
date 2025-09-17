from sqlalchemy import Column, Integer, String, ForeignKey
from model.entity.base import Base
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'course'

    course_id = Column(Integer, primary_key=True)
    student_name=Column(String(30),ForeignKey('student.name'),nullable=False)
    name = Column(String(30),nullable=False)
    teacher = Column(String(30),nullable=False)
    start_date = Column(String,nullable=False)
    end_date = Column(String,nullable=False)
    start_time = Column(String,nullable=False)
    end_time = Column(String,nullable=False)
    type_class=Column(String(10),nullable=False)

    projects = relationship("Project", back_populates="course")
    students = relationship("Student" , back_populates="course")


    def __init__(self, name: object, teacher: object, start_date: object, end_date: object, start_time: object, end_time: object, type_class: object, course_id=None,**kwargs) -> None:
        super().__init__(**kwargs)
        self.course_id = course_id
        self.name = name
        self.teacher = teacher
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.type_class = type_class
        
    def __repr__(self):
        return f"<Course(course_id={self.course_id},name={self.name}, teacher={self.teacher}, type_class={self.type_class})>"




