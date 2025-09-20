from model.entity.attendance import Attendance
from model.service.attendance_service import AttendanceService
from model.tools.decorators import exception_handling


class AttendanceController:
    def __int__(self):
        self.service = AttendanceService()

    @exception_handling
    def save(self, course_id, student_id, session_number, present, class_type):
        attendance = Attendance(course_id, student_id, session_number, present, class_type)
        return self.service.save(attendance)

    @exception_handling
    def edit(self, id, course_id, student_id, session_number, present, class_type):
        attendance = Attendance(course_id, student_id, session_number, present, class_type, id)
        return self.service.edit(attendance)

    @exception_handling
    def delete(self, id):
        return self.service.delete(id)

    def find_all(self):
        try:
            return True, self.service.find_all()
        except Exception as e:
            return False, f"error: {e}"

    def find_by_id(self,id):
        try:
            return True, self.service.find_by_id(id)
        except Exception as e:
            return False, f"error: {e}"