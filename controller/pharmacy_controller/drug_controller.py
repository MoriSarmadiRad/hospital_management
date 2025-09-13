from model.entity.pharmacy_entity.drug import Drug
from model.service.pharmacy_service.drug_service import DrugService
from model.tools.decorators import exception_handling


class DrugController:
    def __init__(self):
        self.service = DrugService()

    @exception_handling
    def save(self, name, manufacturer, dosage_form, price, expiry_date):
        drug = Drug(name, manufacturer, dosage_form, price, expiry_date)
        return self.service.save(drug)

    @exception_handling
    def edit(self,drug_id, name, manufacturer, dosage_form, price, expiry_date):
        drug = Drug(name, manufacturer, dosage_form, price, expiry_date)
        drug.drug_id = drug_id
        return self.service.edit(drug)

    @exception_handling
    def delete(self,drug_id):
        return self.service.delete(drug_id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_id(self,drug_id):
        return self.service.find_by_id(drug_id)