from model.entity.base import Base
from sqlalchemy import Integer, String, Column


class Branch(Base):
    __tablename__ = "branch"
    branch_id=Column(Integer, primary_key=True,nullable=False,unique=True)
    manajer=Column(String(30), nullable=False)
    location=Column(String(30), nullable=False)
    section=Column(String(30), nullable=False)

    def __init__(self,branch_id,manajer,location,section):
        self.branch_id=branch_id
        self.manajer=manajer
        self.location=location
        self.section=section
















