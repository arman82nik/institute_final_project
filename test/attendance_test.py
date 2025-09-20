from controller.attendance_controller import AttendanceController

attendance_controller = AttendanceController()

# save test [passed]
# print(attendance_controller.save(1, 1, 1, 1, "online"))

# edit test [passed]
# print(attendance_controller.edit(1, 1, 1, 2, 0 , "in person"))

# delete test [passed]
# print(attendance_controller.delete(1))

# find all test [passed]
# print(attendance_controller.find_all())

# find by id test [passed]
# print(attendance_controller.find_by_id(1))