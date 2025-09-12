from model.entity.pharmacy_entity.inventory import Inventory
from model.repository.repository import Repository

class InventoryService:

    def __init__(self):
        self.repo = Repository(Inventory)

    def save(self,inventory):
        return self.repo.save(inventory)

    def edit(self,inventory):
        return self.repo.edit(inventory)

    def delete(self,id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,id):
        return self.repo.find_by_id(id)

    def find_by_sample(self,sample):
        pass