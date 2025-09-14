from model.service.financial_service.account_service import *
from model.entity.financial.account import *
from model.tools.decorators import *
from model.tools.validation import *


class AccountController:
    def __init__(self):
        self.service = AccountService()


    @exception_handling
    def save(self, person_name, person_family, birthdate_date, personal_address, account_number, bank_name, bank_branch):
        if validation_name_family(person_name, person_family) and validation_general(bank_name, personal_address, bank_branch) and date_validation(birthdate_date) and validation_account_number(account_number):
            account = Account(person_name, person_family, birthdate_date, personal_address, account_number, bank_name, bank_branch)
            return self.service.save(account)
        else:
            pass


    @exception_handling
    def edit(self, payment_num, transaction_id, payment_id, account_id, person_name, person_family, birthdate_date, personal_address, account_number, bank_name, bank_branch):
        if validation_name_family(person_name, person_family) and validation_general(bank_name, personal_address, bank_branch) and date_validation(birthdate_date) and validation_account_number(account_number):
            account = Account(person_name, person_family, birthdate_date, personal_address, account_number, bank_name, bank_branch)
            account.payment_num = payment_num
            account.transaction_id = transaction_id
            account.payment_id = payment_id
            account.account_id = account_id
            return self.service.edit(account)
        else:
            pass


    @exception_handling
    def delete(self, account_id):
        return self.service.delete(account_id)


    @exception_handling
    def find_by_id(self, account_id):
        return self.service.find_by_account_id(account_id)


    @exception_handling
    def find_all(self):
        return self.service.find_all()