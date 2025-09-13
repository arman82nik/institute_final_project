from model.repository.repository import *
from model.entity.classroom import Classroom



class ClassroomService:
    def __init__(self):
        self.repository = Repository(Classroom)

    def save(self,Classroom):
        return self.repository.save(Classroom)
