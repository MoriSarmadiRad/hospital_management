from model.entity.pharmacy_entity.prescription import Prescription
from model.service.pharmacy_service.prescription_service import PrescriptionService
from model.tools.decorators import exception_handling


class PrescriptionController:
    def __init__(self):
        self.service = PrescriptionService()
