from controller.payment_controller import PaymentController
payment_controller = PaymentController()

#save test
test=payment_controller.save(4343,2000,"it payment","credit card",2/20/2000)
print(test)
#edit test
test=payment_controller.edit(4340,6000,"it payment","credit card",2/20/2000)
print(test)
#delete test
test=payment_controller.delete(2)
print(test)
#find all test
test=payment_controller.find_all()
print(test)
#find_by_id test
test=payment_controller.find_by_id(4343)
print(test)