from controller.student_controller import StudentController

student_controller = StudentController()

#save test
test=student_controller.save(20,"arman","nik","mohsennik1352@gmail.com","male","2/20/2000")
print(test)

#edit test
test=student_controller.edit(20,"ali","alipour","mohsennik1352@gmail.com","female","2/20/2000")
print(test)
#delete_test
test=student_controller.delete(2)
print(test)

#find_all test

test=student_controller.find_all()
print(test)

#find_by_id test
test=student_controller.find_by_id(2)
print(test)