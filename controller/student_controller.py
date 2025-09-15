from model.entity.student import Student
from model.service.student_service import StudentService
from model.tools.decorators import exception_handling


class StudentController:
    def __init__(self):
        self.studentService = StudentService()
    @exception_handling

    def save(self,person_id,name,family,email,gender,birthday):
        student=Student(person_id,name,family,email,gender,birthday)
        self.studentService.save(student)



