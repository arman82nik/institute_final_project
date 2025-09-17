from model.repository import *
from model.entity.course import Course


class CourseService:
    def __init__(self):
        self.repository = Repository(Course)

    def save(self, course):
        return self.repository.save(course)

    def edit(self, course):
        return self.repository.edit(course)

    def delete(self, course_id):
        return self.repository.delete(course_id)

    def find_by_id(self, course_id):
        return self.repository.find_by_id(course_id)

    def find_all(self):
        return self.repository.find_all()
