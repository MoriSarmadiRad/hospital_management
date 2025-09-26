from model.entity.admission.patient import Patient
from model.repository.repository import Repository

class PatientService:
    def __init__(self):
        self.repo = Repository(Patient)

    def save(self,patient):
        return self.repo.save(patient)

    def edit(self,patient):
        return self.repo.edit(patient)

    def delete(self,patient_id):
        return self.repo.delete(patient_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,patient_id):
        return self.repo.find_by_id(patient_id)

