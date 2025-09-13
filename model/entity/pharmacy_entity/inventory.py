from sqlalchemy import Integer,String,Column
from model.entity.base import Base

class Inventory(Base):
    __tablename__="inventory"

    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    drug_id = Column(Integer, nullable=False)
    last_update = Column(String(15), nullable=False)
    quantity = Column(Integer,nullable=False)
    location = Column(String(30))


    def __init__(self, drug_id, last_update, quantity, location):
        self.drug_id = drug_id
        self.last_update = last_update
        self.quantity = quantity
        self.location = location

    def __repr__(self):
        return f"<Inventory(inventory_id={self.inventory_id}, drug_id={self.drug_id},last_update={self.last_update}, quantity={self.quantity}, location='{self.location}')>"

    def to_tuple(self):
        return (
            self.inventory_id,
            self.drug_id,
            self.last_update,
            self.quantity,
            self.location
        )