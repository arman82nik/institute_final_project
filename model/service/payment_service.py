from model.repository.repository import *
from model.entity.payment import Payment

class PaymentService:
    def __init__(self):
        self.repository = Repository(Payment)

    def save(self,payment):
        return self.repository.save(payment)

    def edit(self,payment):
        return self.repository.edit(payment)

    def delete(self,payment):
        return self.repository.delete(payment)

    def find_all(self):
        return self.repository.find_all()


    def find_by_id(self,id):
        return self.repository.find_by_id(id)

