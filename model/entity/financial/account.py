from model.entity.base import Base
from sqlalchemy import String , Integer , Column




class Account(Base):
    __tablename__ = "account"
    payment_num = Column(String(30), primary_key=True, nullable=False, unique=True)
    transaction_id = Column(String(30), primary_key=True, nullable=False, unique=True)
    account_id = Column(String(30), primary_key=True, nullable=False, unique=True, autoincrement=True)
    person_name = Column(String(30), nullable=False)
    person_family = Column(String(30), nullable=False)
    birthdate_date = Column(String(30), nullable=False)
    personal_address = Column(String(30), nullable=False)
    account_number = Column(Integer, nullable=False, unique=True)
    bank_name = Column(String(30), nullable=False)
    bank_branch = Column(String(30), nullable=False)


    def __init__(self, person_name, person_family, birthdate_date, personal_address, account_number, bank_name, bank_branch):
        self.person_name = person_name
        self.person_family = person_family
        self.birthdate_date = birthdate_date
        self.personal_address = personal_address
        self.account_number = account_number
        self.bank_name = bank_name
        self.bank_branch = bank_branch



