from model.repository.repository import *
from model.entity.financial.transaction import *


class TransactionService:
    def __init__(self):
        self.repo = Repository(Transaction)


    def save(self, transaction):
        return self.repo.save(transaction)


    def edit(self, transaction):
        return self.repo.edit(transaction)


    def delete(self, id):
        return self.repo.delete(id)


    def find_by_transaction_id(self, transaction_id):
        return self.repo.find_by_id(transaction_id)


    def find_all(self):
        return self.repo.find_all()