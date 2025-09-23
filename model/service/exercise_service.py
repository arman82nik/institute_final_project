from model.repository import *
from model.entity.exercise import Exercise


class ExerciseService:
    def __init__(self):
        self.repository = Repository(Exercise)

    def save(self, exercise):
        return self.repository.save(exercise)

    def edit(self, exercise):
        return self.repository.edit(exercise)

    def delete(self,id):
        return self.repository.delete(id)

    def find_by_id(self, id):
        return self.repository.find_by_id(id)

    def find_all(self):
        return self.repository.find_all()