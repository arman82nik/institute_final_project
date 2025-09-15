
from model.entity.register import Register
from model.service.register_service import RegisterService
from model.tools.decorators import exception_handling

class RegisterController:
    def __init__(self, register_service):
        self.service = RegisterService()

    @exception_handling
    def save(self,person_id,name,family,phone_number,curse_number):
        register=Register(person_id,name,family,phone_number,curse_number)
        return self.service.save(register)