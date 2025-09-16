from model.repository.repository import *
from model.entity.lesson import Lesson

class LessonService():
    def __init__(self):
        self.repository = Repository(Lesson)

    def save(self,lesson):
        return self.repository.save(lesson)
    def delete(self,lesson):
        return self.repository.delete(lesson)
    def find_by_id(self,id):
        return self.repository.find_by_id(id)
    def find_by(self):
        return self.repository.find_by()
