from model.repository.repository import *
from model.entity.lesson import Lesson

class LessonService:

    def __init__(self):
        self.repository = Repository(Lesson)
    def save(self,lesson):
        return self.repository.save(lesson)
    def edit(self,lesson):
        return self.repository.edit(lesson)

    def delete(self,lesson):
        return self.repository.delete(lesson)
    def find_by_id(self,person_id):
        return self.repository.find_by_id(person_id)
    def find_all(self):
        return self.repository.find_all()
