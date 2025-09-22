from model.service.hos_dep_service.department_service import DepartmentService
from model.tools.decorators import exception_handling
from model.entity.hos_dep.department import Department


class DepartmentController:
    def __init__(self):
        self.service = DepartmentService()

    @exception_handling
    def save(self,surgery,neurology):
        department = Department(surgery,neurology)
        return self.service.save(department)

    @exception_handling
    def edit(self, dep_id, user_id, surgery, neurology, department_id):
        department=Department(dep_id,user_id,surgery,neurology)
        department.department.id = department_id
        return self.service.edit(department)

    @exception_handling
    def delete(self,department_id,dep_id,user_id):
        return self.service.delete(department_id,dep_id,user_id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_department_id(self,department_id):
        return self.service.find_by_department_id(department_id)










