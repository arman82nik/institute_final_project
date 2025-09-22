from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base
from model.entity.student import Student
from model.entity.course import Course


class Exercise(Base):
    __tablename__ = "exercise"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("course.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    session_number = Column(Integer, nullable=False)
    score = Column(Integer, nullable=True)

    student = relationship("student")
    course = relationship("course")

    def __init__(self, course_id, student_id, session_number, score=None, id=None):
        self.id = id
        self.course_id = course_id
        self.student_id = student_id
        self.session_number = session_number
        self.score = score

    def __repr__(self):
        return f"{self.__dict__}"
