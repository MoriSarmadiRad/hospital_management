from model.repository.repository import *
from model.entity.hos_dep.office import *


class OfficeService:
    def __init__(self):
        self.repo = Repository(Office)


    def save(self, office):
        return self.repo.save(office)


    def edit(self, office):
        return self.repo.edit(office)


    def delete(self, office_id):
        return self.repo.delete(office_id)


    def find_by_office_id(self, office_id):
        return self.repo.find_by_id(office_id)


    def find_all(self):
        return self.repo.find_all()