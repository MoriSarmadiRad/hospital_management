from model.entity.base import Base
from sqlalchemy import Integer, String, Column

class Department(Base):
    __tablename__ = "department"
    dep_id = Column(Integer, primary_key=True,nullable=False,unique=True)
    user_id = Column(Integer,primary_key=True,nullable=False,unique=True)

    def __init__(self,dep_id,user_id):
        self.dep_id = dep_id
        self.user_id = user_id


