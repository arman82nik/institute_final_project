from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base
from model.entity.student import Student
from model.entity.course import Course


class Project(Base):
    __tablename__ = "project"


    id = Column(Integer, primary_key=True)
    student_id = Column(Integer,ForeignKey("student.id"),nullable=False)
    course_name=Column(String,ForeignKey("course.name"),nullable=False)
    project_name=Column(String(30),nullable=False)
    file_url=Column(String(255),nullable=False)
    date_time=Column(String,nullable=False)
    score=Column(Integer,nullable=False)


    student = relationship("Student")
    course = relationship("Course")


    def __init__(self,student_id,project_name,file_url,date_time,score,id=None)-> None:
        self.id = id
        self.student_id=student_id
        self.project_name=project_name
        self.file_url=file_url
        self.date_time=date_time
        self.score=score


    def __repr__(self):
        return f"<Project(id={self.id},student_id={self.student_id}, project_name={self.project_name})>"
