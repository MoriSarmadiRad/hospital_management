from model.entity.pharmacy_entity.prescription import Prescription
from model.service.pharmacy_service.prescription_service import PrescriptionService
from model.tools.decorators import exception_handling


class PrescriptionController:
    def __init__(self):
        self.service = PrescriptionService()

    @exception_handling
    def save(self,doctor_id, patient_id, drug_id, date, description,status):
        prescription=Prescription(doctor_id, patient_id, drug_id, date, description,status)
        return self.service.save(prescription)

    @exception_handling
    def edit(self,prescription_id,doctor_id, patient_id, drug_id, date, description,status):
        prescription = Prescription(doctor_id, patient_id, drug_id, date, description,status)
        prescription.prescription_id = prescription_id
        return self.service.edit(prescription)

    @exception_handling
    def delete(self, prescription_id):
        return self.service.delete(prescription_id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_id(self, prescription_id):
        return self.service.find_by_id(prescription_id)