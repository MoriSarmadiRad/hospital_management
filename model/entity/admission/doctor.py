from sqlalchemy import Integer, String, Column
from model.entity.base import Base

class Doctor(Base):
    __tablename__ = "doctor"

    doctor_id = Column(Integer, primary_key=True, autoincrement=True)
    department_id = Column(Integer, nullable=False)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    specialty = Column(String(30), nullable=False)
    department = Column(String(30), nullable=False)
    phone_number = Column(String(30))
    email = Column(String(30))

    def __init__(self, department_id, name, family, specialty, department, phone_number, email):
        self.department_id = department_id
        self.name = name
        self.family = family
        self.specialty = specialty
        self.department = department
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.doctor_id, self.department_id, self.name, self.family, self.specialty, self.department, self.phone_number, self.email))