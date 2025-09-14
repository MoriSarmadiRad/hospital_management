from model.repository.repository import *
from model.entity.financial.payment import *


class PaymentService:
    def __init__(self):
        self.repo = Repository(Payment)


    def save(self, payment):
        return self.repo.save(payment)


    def edit(self, payment):
        return self.repo.edit(payment)


    def delete(self, id):
        return self.repo.delete(id)


    def find_by_payment_id(self, payment_id):
        return self.repo.find_by_id(payment_id)


    def find_all(self):
        return self.repo.find_all()