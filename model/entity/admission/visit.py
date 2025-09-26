from sqlalchemy import Integer, String, Column, ForeignKey
from model.entity.base import Base
from model.entity.admission.doctor import Doctor
from model.entity.admission.time_shift import TimeShift
from model.entity.admission.medical import Medical
from model.entity.admission.patient import Patient

class Visit(Base):
    __tablename__ = "visit"

    visit_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patient.patient_id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctor.doctor_id"), nullable=False)
    medical_id = Column(Integer, ForeignKey("medical.medical_id"), nullable=False)
    shift_id = Column(Integer, ForeignKey("time_shift.shift_id"), nullable=False)
    visit_date = Column(String(30), nullable=False)
    user_id = Column(Integer, nullable=False)

    def __init__(self, patient_id, doctor_id, medical_id, shift_id, visit_date,user_id):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.medical_id = medical_id
        self.shift_id = shift_id
        self.visit_date = visit_date
        self.user_id = user_id

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.visit_id, self.patient_id, self.doctor_id, self.medical_id, self.shift_id, self.visit_date,self.user_id))