from sqlalchemy import Integer,String,Column
from model.entity.base import Base

class Drug(Base):
    __tablename__="drugs"

    drug_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    manufacturer = Column(String(30), nullable=False)
    dosage_form = Column(String(30), nullable=False)
    price = Column(Integer,nullable=False)
    expiry_date = Column(String(30))


    def __init__(self, name, manufacturer, dosage_form, price, expiry_date):
        self.name = name
        self.manufacturer = manufacturer
        self.dosage_form = dosage_form
        self.price = price
        self.expiry_date = expiry_date
