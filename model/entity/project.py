from sqlalchemy import Column, Integer, String, DateTime
from model.entity.base import Base



class Project(Base):
    __tablename__ = "project"


    id = Column(Integer, primary_key=True)
    student_id = Column(Integer,nullable=False)
    project_name=Column(String(30),nullable=False)
    file_url=Column(String(255),nullable=False)
    date_time=Column(DateTime,nullable=False)
    score=Column(Integer,nullable=False)


    def __init__(self,student_id,project_name,file_url,date_time,score):
        self.student_id=student_id
        self.project_name=project_name
        self.file_url=file_url
        self.date_time=date_time
        self.score=score


    def __repr__(self):
        return f"<Project(student={self.student}, project_name={self.project_name})>"
