from model.repository.repository import *
from model.entity.hos_dep.department import *


class DepartmentService:
    def __init__(self):
        self.repo = Repository(Department)


    def save(self, department):
        return self.repo.save(department)


    def edit(self, department):
        return self.repo.edit(department)


    def delete(self, department_id):
        return self.repo.delete(department_id)


    def find_by_department_id(self, department_id):
        return self.repo.find_by_id(department_id)


    def find_all(self):
        return self.repo.find_all()