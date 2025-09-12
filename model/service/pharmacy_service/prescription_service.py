from model.entity.pharmacy_entity.prescription import Prescription
from model.repository.repository import Repository

class PrescriptionService:

    def __init__(self):
        self.repo = Repository(Prescription)

    def save(self,prescription):
        return self.repo.save(prescription)

    def edit(self,prescription):
        return self.repo.edit(prescription)

    def delete(self,id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,id):
        return self.repo.find_by_id(id)

    def find_by_sample(self,sample):
        pass