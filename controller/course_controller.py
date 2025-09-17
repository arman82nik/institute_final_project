from model.entity.course import Course
from model.service import course_service
from model.service.course_service import CourseService
from model.tools.decorators import exception_handling


class CourseController:
    def __init__(self):
        self.service = CourseService()


    @exception_handling
    def save(self,name,teacher,start_date, end_date, start_time, end_time, type_class):
        course = Course(name, teacher, start_date, end_date, start_time, end_time,type_class)
        return self.service.save(course)

    @exception_handling
    def edit(self, course_id, name, teacher, start_date, end_date, start_time, end_time, type_class):
        course= Course(course_id, name,teacher, start_date, end_date, start_time, end_time, type_class)
        course.course_id = course_id
        return self.service.edit(course)


    def delete(self, course_id):
        try:
            return True,self.service.delete(course_id)
        except Exception as e:
            return False, f"error: {e}"

    def find_all(self):
        try:
            return True,self.service.find_all()
        except Exception as e:
            return False, f"error: {e}"

    def find_by_id(self, course_id):
        try:
            return True,self.service.find_by_id(course_id)
        except Exception as e:
            return False, f"error: {e}"





