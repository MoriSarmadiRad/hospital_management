from model.entity.base import Base
from sqlalchemy import Integer, String, Column

class Hospital(Base):
    __tablename__ = 'hospital'
    name = Column(String(30), nullable=False)
    phone_number = Column(Integer,  primary_key=True,nullable=False,unique=True)
    location = Column(String(30), nullable=False)
    section = Column(String(30), nullable=False)

    def __init__(self,name,phone_number,location,section):
        self.name=name
        self.phone_number=phone_number
        self.location=location
        self.section=section