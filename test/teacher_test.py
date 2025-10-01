from controller.teacher_controller import TeacherController
teacher_controller = TeacherController()

#save test
test=teacher_controller.save(4,"ali","alipour","alipour3232@gmail.com","it",4343,"09122335748")
print(test)
#edit test
test=teacher_controller.edit(4,"ali","alipour","alipour3232@gmail.com","english",4342,"09122335748")
print(test)
#delete test
test=teacher_controller.delete(4)
print(test)
#find_all test
test=teacher_controller.find_all()
print(test)
#find_by_id test
test=teacher_controller.find_by_id(4)
print(test)