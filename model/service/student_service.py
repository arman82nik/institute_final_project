from model.repository.repository import Repository
from model.entity.student import Student

class StudentService:
    def __init__(self):
        self.repository = Repository(Student)

    def save(self, student):
        return self.repository.save(student)

    def edit(self, student):
        return self.repository.edit(student)

    def delete(self, student_id):
        return self.repository.delete(student_id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, student_id):
        return self.repository.find_by_id(student_id)