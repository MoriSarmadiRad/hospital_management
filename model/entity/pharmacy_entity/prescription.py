from sqlalchemy import Integer,String,Column
from model.entity.base import Base

class Prescription(Base):
    __tablename__="prescriptions"

    prescription_id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, nullable=False)
    patient_id = Column(Integer, nullable=False)
    drug_id = Column(Integer, nullable=False)
    date = Column(String(15))
    description = Column(String(30))
    status = Column(String(30))

    def __init__(self, doctor_id, patient_id, drug_id, date, description,status):
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.drug_id = drug_id
        self.date = date
        self.description = description
        self.status = status
