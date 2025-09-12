from model.entity.pharmacy_entity.inventory import Inventory
from model.service.pharmacy_service.inventory_service import InventoryService
from model.tools.decorators import exception_handling


class InventoryController:
    def __init__(self):
        self.service = InventoryService()