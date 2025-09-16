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
    def edit(self, id, name, teacher, start_date, end_date, start_time, end_time, type_class):
        course= Course(id, name,teacher, start_date, end_date, start_time, end_time, type_class)
        course.id = id
        return self.service.edit(course)


    def delete(self, id):
        try:
            return True,self.service.delete(id)
        except Exception as e:
            return False, f"error: {e}"

    def find_all(self):
        try:
            return True,self.service.find_all()
        except Exception as e:
            return False, f"error: {e}"

    def find_by_id(self, id):
        try:
            return True,self.service.find_by_id(id)
        except Exception as e:
            return False, f"error: {e}"





