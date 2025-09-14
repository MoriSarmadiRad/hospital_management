from model.repository.repository import *
from model.entity.financial.account import *


class AccountService:
    def __init__(self):
        self.repo = Repository(Account)


    def save(self, account):
        return self.repo.save(account)


    def edit(self, account):
        return self.repo.edit(account)


    def delete(self, account_id):
        return self.repo.delete(account_id)


    def find_by_account_id(self, account_id):
        return self.repo.find_by_id(account_id)


    def find_all(self):
        return self.repo.find_all()