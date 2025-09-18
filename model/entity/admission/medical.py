from sqlalchemy import Integer , String , Column
from model.entity.base import Base


class Medical(Base):
    __tablename__ = "medical"

    medical_id = Column(Integer,primary_key=True,autoincrement=True)
    type = Column(String(30),nullable=False)
    description = Column(String(30),nullable=False)

    def __int__(self,type,description):
        self.type = type
        self.description = description

    def __repr__(self):
       return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.medical_id , self.type , self.description))