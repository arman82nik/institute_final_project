from controller.attendance_controller import AttendanceController

attendance_controller = AttendanceController()

# save test [passed]
# print(attendance_controller.save(1, 1, 1, 1, "online"))

# edit test []
print(attendance_controller.edit(1, 1, 1, 2, 0 , "in person"))
