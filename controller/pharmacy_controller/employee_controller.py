from model.entity.pharmacy_entity.employee import Employee
from model.service.pharmacy_service.employee_service import EmployeeService
from model.tools.decorators import exception_handling


class EmployeeController:
    def __init__(self):
        self.service = EmployeeService()