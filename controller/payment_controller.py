from model.entity.payment import Payment
from model.service.payment_service import PaymentService
from model.tools.decorators import exception_handling

class PaymentController:
    def __init__(self):
        self.service = PaymentService()

    @exception_handling
    def save(self,person_id,amount,title,payment_type,payment_date,description):
        payment = Payment(person_id,amount,title,payment_type,payment_date,description)
        self.service.save(payment)

    @exception_handling
    def edit(self,person_id,amount,title,payment_type,payment_date,description):
        payment = Payment(person_id,amount,title,payment_type,payment_date,description)
        self.service.edit(payment)
    def delete(self,person_id):
        try:
            return True, self.service.delete(id)
        except Exception as e:
            return False, f"error: {e}"

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


