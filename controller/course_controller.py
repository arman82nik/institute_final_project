from model.entity.course import Course
from model.service.course_service import CourseService
from model.tools.decorators import exception_handling


class CourseController:
    def __init__(self):
        self.service = CourseService()


    @exception_handling
    def save(self,name,teacher,start_date, end_date, start_time, end_time, type_class):
        course = Course(name, teacher, start_date, end_date, start_time, end_time, type_class)
        return self.service.save(course)


