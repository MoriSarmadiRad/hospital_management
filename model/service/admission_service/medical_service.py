from model.entity.admission.medical import Medical
from model.repository.repository import Repository


class MedicalService :
    def __init__(self):
        self.repo = Repository(Medical)


    def save(self,medical):
        return self.repo.save(medical)

    def edit(self,medical):
        return self.repo.edit(medical)

    def delete(self,medical_id):
        return self.repo.delete(medical_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,medical_id):
        return self.repo.find_by_id(medical_id)

    def find_by_medical_id_and_type(self,medical_id,type):
        return self.repo.find_by(and_(Medical.medical_id.like(medical_id + "%"), Medical.type.like(type + "%")))
