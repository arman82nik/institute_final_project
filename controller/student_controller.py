from model.entity.student import Student
from model.service.student_service import StudentService
from model.tools.decorators import exception_handling


class StudentController:
    def __init__(self):
        self.service = StudentService()
    @exception_handling

    def save(self,student_id,name,family,email,gender,birthday):
        student=Student(student_id,name,family,email,gender,birthday)
        self.service.save(student)

    @exception_handling
    def edit(self,id,student_id,name,family,email,gender,birthday):
        student=Student(student_id,name,family,email,gender,birthday)
        student.id=id
        self.service.edit(student)

    def delete(self,student_id):
        try:
            return True, self.service.delete(student_id)
        except Exception as e:
            return False, f"error: {e}"

    def find_all(self):
        try:
            return True, self.service.find_all()
        except Exception as e:
            return False, f"error: {e}"

    def find_by_id(self,student_id):
        try:
            return True, self.service.find_by_id(student_id)
        except Exception as e:
            return False, f"error: {e}"





