from sqlalchemy import Integer,String,Column
from model.entity.base import Base

class Inventory(Base):
    __tablename__="inventory"

    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    drug_id = Column(Integer, nullable=False)
    last_updatet = Column(String(15), nullable=False)
    quantity = Column(Integer,nullable=False)
    location = Column(String(30))


    def __init__(self, drug_id, last_updatet, quantity, location):
        self.drug_id = drug_id
        self.last_updatet = last_updatet
        self.quantity = quantity
        self.location = location