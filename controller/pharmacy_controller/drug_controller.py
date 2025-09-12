from model.entity.pharmacy_entity.drug import Drug
from model.service.pharmacy_service.drug_service import DrugService
from model.tools.decorators import exception_handling


class DrugController:
    def __init__(self):
        self.service = DrugService()