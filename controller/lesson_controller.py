from model.entity.lesson import Lesson
from model.service.lesson_service import LessonService
from model.tools.decorators import exception_handling



class LessonController:
    def __init__(self):
        self.service=LessonService()


    @exception_handling

    def save(self,person_id, title, code, teacher, units):
        lesson=Lesson(person_id, title, code, teacher, units)
        return self.service.save(lesson)

    @exception_handling


    def edit(self,id,person_id, title, code, teacher, units):
        lesson=Lesson(id,person_id, title, code, teacher, units)
        lesson.id=id
        return self.service.edit(lesson)


    def delete(self,person_id):
        try:
            return True,self.service.delete(person_id)
        except Exception as e:
            return False, f"error: {e}"


    def find_all(self):
        try:
            return True,self.service.find_all()
        except Exception as e:
            return False, f"error: {e}"


    def find_by_id(self, person_id):
        try:
            return True,self.service.find_by_id(person_id)
        except Exception as e:
            return False, f"error: {e}"