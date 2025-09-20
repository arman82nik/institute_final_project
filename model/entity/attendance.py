from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base
from model.entity.student import Student
from model.entity.course import Course


class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("course.course.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    session_number = Column(Integer, nullable=False)
    present = Column(Integer, nullable=False)
    class_type = Column(String(20), nullable=False)

    student = relationship("Student")
    course = relationship("Course")

    def __init__(self, course_id, student_id, session_number, present, class_type, id=None ):
        self.id = id
        self.course_id = course_id
        self.student_id = student_id
        self.session_number = session_number
        self.present = present
        self.class_type = class_type

    def __repr__(self):
        return f"{self.__dict__}"