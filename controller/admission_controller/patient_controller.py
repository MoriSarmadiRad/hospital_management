from model.tools.decorators import exception_handling
from model.service.admission_service.patient_service import PatientService
from model.entity.admission.patient import Patient


class PatientController:
    def __init__(self):
        self.service = PatientService()


    @exception_handling
    def save(self,name,family,age,gender,phone_number,address,national_code):
        patient = Patient(name,family,age,gender,phone_number,address,national_code)
        return self.service.save(patient)

    @exception_handling
    def edit(self,patient_id,name,family,age,gender,phone_number,address,national_code):
        patient = Patient(name,family,age,gender,phone_number,address,national_code)
        patient.patient_id = patient_id
        return self.service.edit(patient)


    @exception_handling
    def delete(self,patient_id):
        return self.service.delete(patient_id)

    @exception_handling
    def find_by_id(self,patient_id):
        patient = self.service.find_by_id(patient_id)
        return patient

    @exception_handling
    def find_all(self):
        return self.service.find_all()


    @exception_handling
    def find_by_family_and_gender(self,family,gender):
        return self.service.find_by_family_and_gender(family,gender)