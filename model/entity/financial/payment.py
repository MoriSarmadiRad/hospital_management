from model.entity.base import Base
from sqlalchemy import String , Integer , Column




class Payment(Base):
    __tablename__ = "payment"
    payment_num = Column(String(30), primary_key=True, nullable=False , unique=True)
    transaction_id = Column(String(30), primary_key=True, nullable=False, unique=True)
    payment_id = Column(String(30), primary_key=True, nullable=False, autoincrement=True)
    amount = Column(Integer, nullable=False)
    payment_type = Column(String(30), nullable=False)
    date_time = Column(String(30), nullable=False)
    description = Column(String(300), nullable=False)


    def __init__(self, amount, payment_type, date_time, description):
        self.amount = amount
        self.payment_type = payment_type
        self.date_time = date_time
        self.description = description
