from model.service.financial_service.payment_service import *
from model.entity.financial.payment import *
from model.tools.decorators import *
from model.tools.validation import *


class PaymentController:
    def __init__(self):
        self.service = PaymentService()


    @exception_handling
    def save(self, amount, payment_type, date_time, description ):
        if validation_general(payment_type,date_time,description) and date_validation(date_time):
            payment = Payment(amount, payment_type, date_time, description)
            return self.service.save(payment)
        else:
            pass


    @exception_handling
    def edit(self, payment_num, transaction_id, payment_id, amount, payment_type, date_time, description ):
        if validation_general(payment_type,date_time,description) and date_validation(date_time):
            payment = Payment(amount, payment_type, date_time, description)
            payment.payment_num = payment_num
            payment.transaction_id = transaction_id
            payment.payment_id = payment_id
            return self.service.edit(payment)
        else:
            pass


    @exception_handling
    def delete(self, payment_id):
        return self.service.delete(payment_id)


    @exception_handling
    def find_by_payment_id(self, payment_id):
        return self.service.find_by_payment_id(payment_id)


    @exception_handling
    def find_all(self):
        return self.service.find_all()




