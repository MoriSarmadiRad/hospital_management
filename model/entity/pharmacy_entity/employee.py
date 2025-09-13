from sqlalchemy import Integer,String,Column
from model.entity.base import Base

class Employee(Base):
    __tablename__="employees"

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    department_id = Column(Integer, nullable=False)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    role = Column(String(20),nullable=False)
    email = Column(String(30))
    hire_date(Column(String(15)))
    description=Column(String(30))


    def __init__(self,department_id, name, family, role, email, hire_date,description):
        self.department_id = department_id
        self.name = name
        self.family = family
        self.role = role
        self.email = email
        self.hire_date = hire_date
        self.description = description