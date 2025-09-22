from model.entity.teacher import Teacher
from model.service.teacher_service import TeacherService
from model.tools.decorators import exception_handling


class TeacherController:
    def __init__(self):
        self.service = TeacherService()
    @exception_handling

    def save(self,first_name, last_name, email, department, national_id, phone_number):
        teacher=Teacher(first_name, last_name, email, department, national_id, phone_number)
        self.service.save(teacher)
    @exception_handling


    def edit(self,first_name, last_name, email, department, national_id, phone_number):
        teacher=Teacher(first_name, last_name, email, department, national_id, phone_number)
        teacher.id=id
        self.service.edit(teacher)

    def delete(self,national_id):
        try:
            return True, self.service.delete(id)
        except Exception as e:
            return False, f"error: {e}"

    def find_all(self):
        try:
            return True, self.service.find_all()
        except Exception as e:
            return False, f"error: {e}"

    def find_by_id(self,id):
        try:
            return True, self.service.find_by_id(id)
        except Exception as e:
            return False, f"error: {e}"

