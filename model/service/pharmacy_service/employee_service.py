from model.entity.pharmacy_entity.employee import Employee
from model.repository.repository import Repository

class EmployeeService:

    def __init__(self):
        self.repo = Repository(Employee)

    def save(self,employee):
        return self.repo.save(employee)

    def edit(self,employee):
        return self.repo.edit(employee)

    def delete(self,id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,id):
        return self.repo.find_by_id(id)

    def find_by_sample(self,sample):
        pass