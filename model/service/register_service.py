from model.repository.repository import *
from model.entity.register import Register



class RegisterService:
    def __init__(self):
        self.repository = Repository(Register)


    def save(self,register):
        self.repository.save(register)

    def delete(self,student_id):
        self.repository.delete(student_id)

    def find_by_id(self,student_id):
        return self.repository.find_by_id(student_id)

    def find_by(self,register):
        return self.repository.find_by(register)

