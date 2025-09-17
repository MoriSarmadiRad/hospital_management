from model.entity.admission.doctor import Doctor
from model.service.admission_service.doctor_service import DoctorService
from model.tools.decorators import exception_handling


class DoctorController:
    def __init__(self):
        self.service = DoctorService()

    @exception_handling
    def save(self,name,family,specialty,department,phone_number,email):
        doctor = Doctor(name,family,specialty,department,phone_number,email)
        return self.service.save(doctor)

    @exception_handling
    def edit(self,doctor_id,name,family,specialty,department,phone_number,email):
        doctor = Doctor(name,family,specialty,department,phone_number,email)
        doctor.doctor_id = doctor_id
        return self.service.edit(doctor)

    @exception_handling
    def delete(self,doctor_id):
        return self.service.delete(doctor_id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_id(self,doctor_id):
        doctor = self.service.find_by_id(doctor_id)
        return doctor

    @exception_handling
    def find_by_family_and_specialty(self, family, specialty):
        return self.service.find_by_family_and_specialty(family,specialty)