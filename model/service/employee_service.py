from model.entity.teacher import Teacher
from model.repository.repository import *
from model.entity.employee import Employee

class EmployeeService:
    def __init__(self):
        self.repository = Repository(Teacher)

    def save(self,Teacher):
        return self.repository.save(Teacher)

    def delete(self,national_id):
        return self.repository.delete(national_id)

    def edit(self,Teacher):
        return self.repository.edit(Teacher)

    def find_all(self):
        return self.repository.find_all()
    def find_by_id(self,national_id):
        return self.repository.find_by_id(national_id)

    def find_by_id(self,national_id):
        return self.repository.find_by_id(national_id)