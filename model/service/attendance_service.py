from model.repository import *
from model.entity.attendance import Attendance


class AttendanceService:
    def __init__(self):
        self.repository = Repository(Attendance)

    def save(self, attendance):
        return self.repository.save(attendance)

    def edit(self,attendance):
        return self.repository.edit(attendance)

    def delete(self, id):
        return self.repository.delete(id)

    def find_by_id(self, id):
        return self.repository.find_by_id(id)

    def find_all(self):
        return self.repository.find_all()
