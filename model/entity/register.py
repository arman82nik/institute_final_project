from sqlalchemy import  Integer, String, Column
from model.entity.base import Base


class Register(Base):
    __tablename__ = "register"


    person_id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    family = Column(String,nullable=False)
    phone_number = Column(Integer,nullable=False)
    curse_number = Column(String,nullable=False)

    def __init__(self,person_id,name,family,phone_number,curse_number):
        self.person_id = person_id
        self.name = name
        self.family = family
        self.phone_number = phone_number
        self.curse_number = curse_number

    def __repr__(self):
        return f"{self.__dict__}"
    #sina































#class Register:
    #def __init__(self,id,person_id,name,family,phone_number,curse_number):
        #self.id = id
        #self.person_id = person_id
        #self.name = name
        #self.family = family
        #self.phone_number = phone_number
        #self.curse_number = curse_number

    #def __repr__(self):
        #return f"{self.__dict__}"

    #def to_tuple(self):
       # return tuple((self.id, self.person_id, self.name, self.family, self.phone_number, self.curse_number))