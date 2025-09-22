from model.repository.repository import *
from model.entity.student import Student

class StudentService:
    def __init__(self):
        self.repository = Repository(Student)

    def save(self,student):
        return self.repository.save(student)

    def delete(self,person_id):
        return self.repository.delete(person_id)

    def edit(self,student):
        return self.repository.edit(student)

    def find_all(self):
        return self.repository.find_all()
    def find_by_id(self,person_id):
        return self.repository.find_by_id(person_id)
