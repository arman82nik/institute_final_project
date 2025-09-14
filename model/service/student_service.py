from model.repository.repository import *
from model.entity.student import Student

class StudentService:
    def __init__(self):
        self.repository = Repository(Student)

    def save(self,student):
        return self.repository.save(student)