from controller.register_controller import RegisterController
register_controller = RegisterController()

#save test
test=register_controller.save(4343,"mohammad","rezaei","09122335748",309)
print(test)
#edit test
test=register_controller.edit(4343,"ali","rezaei","09122335748",309)
print(test)
#delete test
test=register_controller.delete(2)
print(test)
#find all test
test=register_controller.find_all()
print(test)
#find_by_id test
test=register_controller.find_by_id(4343)
print(test)