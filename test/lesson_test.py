from controller.lesson_controller import LessonController

lesson_controller = LessonController()

#save test
test=lesson_controller.save(232323,"math",309,"alipour",18)
print(test)
#delete test
test=lesson_controller.delete(4)
print(test)
#edit test
test=lesson_controller.edit(232323,"math",309,"alipour",19)
print(test)
#find_all test
test=lesson_controller.find_all()
print(test)
#find_by_id test
test=lesson_controller.find_by_id(2)
print(test)
