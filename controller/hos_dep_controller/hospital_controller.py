from model.entity.hos_dep.hospital import Hospital
from model.service.hos_dep_service.hospital_service import HospitalService
from model.tools.decorators import *

class HospitalController:
    def __init__(self):
        self.service = HospitalService()

    @exception_handling
    def save(self,name,phone_number,location,section):
        hospital=Hospital(name,phone_number,location,section)
        return self.service.save(hospital)

    @exception_handling
    def edit(self,name,phone_number,hospital_id,location,section):
        hospital=Hospital(name,phone_number,location,section)
        hospital.hospital_id=hospital_id
        return self.service.edit(hospital)

    @exception_handling
    def delete(self,name,phone_number,location,section):
        return self.service.delete(name,phone_number,location,section)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_hospital_id(self,hospital_id):
        return self.service.find_by_id(hospital_id)





