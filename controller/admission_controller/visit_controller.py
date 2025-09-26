from model.entity.admission.visit import Visit
from model.service.admission_service.visit_service import VisitService
from model.tools.decorators import exception_handling


class VisitController:
    def __init__(self):
        self.service = VisitService

    @exception_handling
    def save(self,patient_id,medical_id,time_shift_id,user_id):
        visit = Visit(patient_id,medical_id,time_shift_id,user_id)
        return self.service.save(visit)

    @exception_handling
    def edit(self,visit_id ,patient_id,medical_id,time_shift_id,user_id):
        visit = Visit(patient_id,medical_id,time_shift_id,user_id)
        visit.visit_id = visit_id
        return self.service.edit(visit)

