from model.entity.exercise import Exercise
from model.service.exercise_service import ExerciseService
from model.tools.decorators import exception_handling


class ExerciseController:
    def __init__(self):
        self.service = ExerciseService()

    @exception_handling
    def save(self, course_id, student_id, session_number, score=None):
        exercise = Exercise(course_id, student_id, session_number, score)
        return self.service.save(exercise)

    @exception_handling
    def edit(self, id, course_id, student_id, session_number, score=None):
        exercise = Exercise(course_id, student_id, session_number, score, id)
        return self.service.edit(exercise)

    @exception_handling
    def delete(self, id):
        return self.service.delete(id)

    def find_all(self, id):
        try:
            return True, self.service.find_all()
        except Exception as e:
            return False, f"error: {e}"

    def find_by_id(self, id):
        try:
            return True, self.service.find_by_id(id)
        except Exception as e:
            return False, f"error: {e}"