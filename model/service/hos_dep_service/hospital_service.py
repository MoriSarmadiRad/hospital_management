from model.repository.repository import *
from model.entity.hos_dep.hospital import *


class HospitalService:
    def __init__(self):
        self.repo = Repository(Hospital)


    def save(self, hospital):
        return self.repo.save(hospital)


    def edit(self, hospital):
        return self.repo.edit(hospital)


    def delete(self, hospital_id):
        return self.repo.delete(hospital_id)


    def find_by_hospital_id(self, hospital_id):
        return self.repo.find_by_id(hospital_id)


    def find_all(self):
        return self.repo.find_all()