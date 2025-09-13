from model.entity.classroom import Classroom
from model.service.classroom_service import ClassroomService
from model.tools.decorators import exception_handling


class ClassroomController:
    def __init__(self):
        self.service = ClassroomService()


    @exception_handling
    def save(self,name,teacher,start_date, end_date, start_time, end_time, type_class):
        classroom = Classroom(name, teacher, start_date, end_date, start_time, end_time, type_class)
        return self.service.save(classroom)


