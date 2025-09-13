from sqlalchemy import Integer, String, Column
from model.entity.base import Base


class Drug(Base):
    __tablename__ = "drugs"

    drug_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    manufacturer = Column(String(30), nullable=False)
    dosage_form = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)
    expiry_date = Column(String(30))

    def __init__(self, name: str, manufacturer: str, dosage_form: str, price: int, expiry_date: str):
        self.name = name
        self.manufacturer = manufacturer
        self.dosage_form = dosage_form
        self.price = price
        self.expiry_date = expiry_date

    def __repr__(self):
        return f"<Drug(drug_id={self.drug_id}, name='{self.name}', manufacturer='{self.manufacturer}', price={self.price}, expiry_date='{self.expiry_date}')>"

    def to_tuple(self):
        return (
            self.drug_id,
            self.name,
            self.manufacturer,
            self.price,
            self.expiry_date
        )