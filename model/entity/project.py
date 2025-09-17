from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base


class Project(Base):
    __tablename__ = "project"


    project_id = Column(Integer, primary_key=True)
    student_id = Column(Integer,ForeignKey("student.id"),nullable=False)
    course_name=Column(String,ForeignKey("course.name"),nullable=False)
    project_name=Column(String(30),nullable=False)
    file_url=Column(String(255),nullable=False)
    date_time=Column(String,nullable=False)
    score=Column(Integer,nullable=False)


    student = relationship("Student",back_populates="projects")
    course = relationship("Course" ,back_populates="projects")


    def __init__(self,student_id,project_name,course_name,file_url,date_time,score,project_id= None,**kwargs)-> None:
        super().__init__(**kwargs)
        self.project_id = project_id
        self.student_id=student_id
        self.course_name= course_name
        self.project_name=project_name
        self.file_url=file_url
        self.date_time=date_time
        self.score=score


    def __repr__(self):
        return f"<Project(project_id={self.project_id},student_id={self.student_id}, project_name={self.project_name})>"
