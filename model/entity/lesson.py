from sqlalchemy import  Integer, String, Column
from model.entity.base import Base
from sqlalchemy.orm import relationship



class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    code = Column(String, nullable=False)
    teacher = Column(String, nullable=False)
    units = Column(Integer, nullable=False)


    registers=relationship("Register", back_populates="lessons")
    teachers=relationship("Teacher", back_populates="lessons")

    def __init__(self, person_id:None, title:object, code:object, teacher:object, units:object,**kwargs):

        super().__init__(**kwargs)

        self.person_id = person_id
        self.title = title
        self.code = code
        self.teacher = teacher
        self.units = units

    def __repr__(self):
        return f"<Lesson(person_id={self.person_id},title{self.title},code={self.code}, teacher={self.teacher})>"

