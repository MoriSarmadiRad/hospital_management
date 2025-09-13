from model.entity.pharmacy_entity.inventory import Inventory
from model.service.pharmacy_service.inventory_service import InventoryService
from model.tools.decorators import exception_handling


class InventoryController:
    def __init__(self):
        self.service = InventoryService()

    @exception_handling
    def save(self,drug_id, last_update, quantity, location):
        inventory=Inventory(drug_id, last_update, quantity, location)
        return self.service.save(inventory)

    @exception_handling
    def edit(self, drug_id, last_update, quantity, location, inventory_id):
        inventory = Inventory(drug_id, last_update, quantity, location)
        inventory.inventory_id = inventory_id
        return self.service.edit(inventory)

    @exception_handling
    def delete(self, drug_id):
        return self.service.delete(drug_id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_inventory_id(self, drug_id):
        return self.service.find_by_id(drug_id)