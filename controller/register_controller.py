
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


    @exception_handling

    def edit(self,id,person_id,name,family,phone_number,curse_number):
        register=Register(id,person_id,name,family,phone_number,curse_number)
        register.id=id
        return self.service.edit(register)

    def delete(self, id):
        try:
            return True,self.service.delete(id)
        except Exception as e:
            return False, f"error: {e}"


    def find_all(self):
        try:
            return True,self.service.find_all()
        except Exception as e:
            return False, f"error: {e}"


    def find_by_id(self, id):
        try:
            return True,self.service.find_by_id(id)
        except Exception as e:
            return False, f"error: {e}"