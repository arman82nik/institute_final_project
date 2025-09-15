from model.repository import *
from model.entity.course import Course



class CourseService:
    def __init__(self):
        self.repository = Repository(Course)

    def save(self,course):
        return self.repository.save(course)
