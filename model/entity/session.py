from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base


class Session(Base):
    __tablename__ = "session"
    id = Column(Integer, primary_key=True)
    class_number = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    course = Column(String(30), nullable=False)
    teacher = Column(String(30), nullable=False)

    classroom = relationship("Classroom", back_populates="sessions")
    attendance = relationship("Attendance", back_populates="sessions")
    exercise = relationship("Exercise", back_populates="sessions")

    def __init__(self, class_number:object,floor:object,
                 start_time:object,end_time:object,
                 start_date:object,end_date:object,
                 course:object,teacher:object, **kwargs):
        super().__init__(**kwargs)
        self.class_number = class_number
        self.floor = floor
        self.start_time = start_time
        self.end_time = end_time
        self.start_date = start_date
        self.end_date = end_date
        self.course = course
        self.teacher = teacher



    def __repr__(self):
        return (f"<session({self.class_number}, {self.start_time}, "
                f"{self.end_time},{self.course}, {self.teacher})>")