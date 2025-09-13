from sqlalchemy import Integer,String,Column
from model.entity.base import Base

class Order(Base):
    __tablename__="orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    prescription_id = Column(Integer, nullable=False)
    payment_num = Column(Integer, nullable=False)
    drug_id = Column(Integer, nullable=False)
    employee_id = Column(Integer, nullable=False)
    order_date = Column(String(15))
    total_amount = Column(Integer, nullable=False)
    description = Column(String(30))

    def __init__(self, prescription_id, payment_num, drug_id, employee_id,order_date,total_amount, description):
        self.prescription_id = prescription_id
        self.payment_num = payment_num
        self.drug_id = drug_id
        self.employee_id = employee_id
        self.order_date = order_date
        self.total_amount = total_amount
        self.description = description

    def __repr__(self):
        return f"<Order(id={self.order_id}, prescription_id={self.prescription_id}, payment_num={self.payment_num}, drug_id={self.drug_id}, employee_id={self.employee_id}, order_date={self.order_date}, total_amount={self.total_amount}, description='{self.description}')>"

    def to_tuple(self):
        return (
            self.order_id,
            self.prescription_id,
            self.payment_num,
            self.drug_id,
            self.employee_id,
            self.order_date,
            self.total_amount,
            self.description
        )