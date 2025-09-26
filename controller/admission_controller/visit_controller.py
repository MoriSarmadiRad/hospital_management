from model.entity.admission.visit import Visit
from model.service.admission_service.visit_service import VisitService
from model.tools.decorators import exception_handling


class VisitController:
    def __init__(self):
        self.service = VisitService()

    @exception_handling
    def save(self,patient_id,doctor_id,medical_id,shift_id,visit_date,user_id):
        visit = Visit(patient_id,doctor_id,medical_id,shift_id,visit_date,user_id)
        return self.service.save(visit)

    @exception_handling
    def edit(self,visit_id,patient_id,doctor_id,medical_id,shift_id,visit_date,user_id):
        visit = Visit(patient_id,doctor_id,medical_id,shift_id,visit_date,user_id)
        visit.visit_id = visit_id
        return self.service.edit(visit)

    @exception_handling
    def delete(self, visit_id):
        return self.service.delete(visit_id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_id(self, visit_id):
        visit = self.service.find_by_id(visit_id)
        return visit

    @exception_handling
    def find_by_user_id_and_doctor_id(self, user_id, doctor_id):
        return self.service.find_by_user_id_and_doctor_id(user_id, doctor_id)
