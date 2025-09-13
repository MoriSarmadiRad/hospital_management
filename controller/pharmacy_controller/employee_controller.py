from model.entity.pharmacy_entity.employee import Employee
from model.service.pharmacy_service.employee_service import EmployeeService
from model.tools.decorators import exception_handling


class EmployeeController:
    def __init__(self):
        self.service = EmployeeService()

    @exception_handling
    def save(self,department_id, name, family, role, email, hire_date, description):
        employee=Employee(department_id,name, family, role, email, hire_date, description)
        return self.service.save(employee)

    @exception_handling
    def edit(self, department_id, name, family, role, email, hire_date, description):
        employee = Employee(department_id, name, family, role, email, hire_date, description)
        return self.service.edit(employee)

    @exception_handling
    def delete(self, department_id):
        return self.service.delete(department_id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_id(self, department_id):
        return self.service.find_by_id(department_id)