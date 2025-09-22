from model.entity.employee import Employee
from model.service.employee_service import EmployeeService
from model.tools.decorators import exception_handling

class EmployeeController:
    def __init__(self):
        self.service = EmployeeService()

    @exception_handling

    def save(self,first_name,last_name,national_id,birthday,email,job_title,department,hire_date,salary):
        employee=Employee(first_name,last_name,national_id,birthday,email,job_title,department,hire_date,salary)
        self.service.save(employee)

    @exception_handling

    def edit(self,first_name,last_name,national_id,birthday,email,job_title,department,hire_date,salary):
        employee=Employee(first_name,last_name,national_id,birthday,email,job_title,department,hire_date,salary)
        employee.id=id

        self.service.edit(employee)

    def delete(self,employee_id):
        try:
            return True, self.service.delete(id)
        except Exception as e:
            return False, f"error: {e}"
    def find_all(self):
        try:
            return True, self.service.find_by_id(id)
        except Exception as e:
            return False, f"error: {e}"