from model.entity.student import Student
from model.service.student_service import StudentService
from model.tools.decorators import exception_handling

class StudentController:
    def __init__(self):
        self.service = StudentService()

    @exception_handling
    def save(self, student_id, name, age, gender, birthday, email):
        student = Student(student_id, name, age, gender, birthday, email)
        return self.service.save(student)

    @exception_handling
    def edit(self, id, student_id, name, age, gender, birthday, email):
        student = Student(student_id, name, age, gender, birthday, email)
        student.id = id
        return self.service.edit(student)

    @exception_handling
    def delete(self, student_id):
        return self.service.delete(student_id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_id(self, student_id):
        return self.service.find_by_id(student_id)





