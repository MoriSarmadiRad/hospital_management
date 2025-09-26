from sqlalchemy import Integer,String,Column
from model.entity.base import Base

class Patient(Base):
    __tablename__ = "patient"

    patient_id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(30),nullable=False)
    family = Column(String(30),nullable=False)
    age = Column(Integer)
    gender = Column(String(20),nullable=False)
    phone_number = Column(String(30),nullable=False)
    address = Column(String(30))
    national_code = Column(String(30))


    def __init__(self,name,family,age,gender,phone_number,address,national_code):
        self.name = name
        self.family = family
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.address = address
        self.national_code = national_code


    def __repr__(self):
        return f"{self.__dict__}"


    def to_tuple(self):
        return tuple(
            (self.patient_id , self.name , self.family , self.age , self.gender , self.phone_number , self.address , self.national_code)
        )
