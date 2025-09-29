from model.repository.repository import *
from model.entity.employee import Employee

class EmployeeService:
    def __init__(self):
        self.repository = Repository(Employee)

    def save(self,employee):
        return self.repository.save(employee)

    def delete(self,national_id):
        return self.repository.delete(national_id)

    def edit(self,employee):
        return self.repository.edit(employee)

    def find_all(self):
        return self.repository.find_all()
    def find_by_id(self,national_id):
        return self.repository.find_by_id(national_id)

