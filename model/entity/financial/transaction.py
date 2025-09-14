from model.entity.base import Base
from sqlalchemy import String , Column




class Transaction(Base):
    __tablename__ = "transaction"
    payment_num = Column(String(30), primary_key=True , nullable=False , unique=True)
    transaction_id = Column(String(30), primary_key=True , nullable=False , unique=True, autoincrement=True)


    def __init__(self, payment_num, transaction_id):
        self.payment_num = payment_num
        self.transaction_id = transaction_id






