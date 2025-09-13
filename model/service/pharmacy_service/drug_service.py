from model.entity.pharmacy_entity.drug import Drug
from model.repository.repository import Repository

class DrugService:

    def __init__(self):
        self.repo = Repository(Drug)

    def save(self,drug):
        return self.repo.save(drug)

    def edit(self,drug):
        return self.repo.edit(drug)

    def delete(self,id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,id):
        return self.repo.find_by_id(id)

    def find_by_sample(self,sample):
        pass