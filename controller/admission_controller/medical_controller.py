from model.tools.decorators import exception_handling
from model.service.admission_service.medical_service import MedicalService
from model.entity.admission.medical import Medical

class MedicalController:
    def __init__(self):
        self.service = MedicalService()

    @exception_handling
    def save(self,type,description):
        medical = Medical(type,description)
        return self.service.save(medical)


    @exception_handling
    def edit(self,medical_id,type,description):
        medical = Medical(type,description)
        medical.medical_id = medical_id
        return self.service.edit(medical)


    @exception_handling
    def delete(self,medical_id):
        return self.service.delete(medical_id)


    @exception_handling
    def find_by_id(self,medical_id):
        medical = self.service.find_by_id(medical_id)
        return medical
