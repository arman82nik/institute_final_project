from model.repository.repository import *
from model.entity.teacher import Teacher


class TeacherService:
    def __init__(self):
        self.repository = Repository(Teacher)

    def save(self,student):
        self.repository.save(student)


    def delete(self,national_id):
        self.repository.delete(national_id)

    def edit(self,teacher):
        self.repository.edit(teacher)

    def find_all(self):
        self.repository.find_all()

    def find_by_id(self,id):
        self.repository.find_by(id)