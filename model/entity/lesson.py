from sqlalchemy import  Integer, String, Column
from model.entity.base import Base



class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    code = Column(String, nullable=False)
    teacher = Column(String, nullable=False)
    units = Column(String, nullable=False)


    def __init__(self, person_id, title, code, teacher, units):
        self.person_id = person_id
        self.title = title
        self.code = code
        self.teacher = teacher
        self.units = units



    def __repr__(self):
        return f"{self.__dict__}"

