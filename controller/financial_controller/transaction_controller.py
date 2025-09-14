from model.service.financial_service.transaction_service import TransactionService
from model.tools.decorators import *
from model.entity.financial.transaction import *


class TransactionController:
    def __init__(self):
        self.service = TransactionService()


    @exception_handling
    def save(self, payment_num, transaction_id):
        transaction = Transaction(payment_num, transaction_id)
        return self.service.save(transaction)


    @exception_handling
    def edit(self, payment_num, transaction_id):
        transaction = Transaction(payment_num, transaction_id)
        return self.service.edit(transaction)


    @exception_handling
    def delete(self, transaction_id):
        return self.service.delete(transaction_id)


    @exception_handling
    def find_by_transaction_id(self, transaction_id):
        return self.service.find_by_transaction_id(transaction_id)


    @exception_handling
    def find_all(self):
        return self.service.find_all()

