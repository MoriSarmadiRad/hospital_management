from model.entity.admission.doctor import Doctor
from model.repository.repository import Repository

class DoctorService:
    def __init__(self):
        self.repo = Repository(Doctor)

    def save(self,doctor):
        return self.repo.save(doctor)

    def edit(self,doctor):
        return self.repo.edit(doctor)

    def delete(self,doctor_id):
        return self.repo.delete(doctor_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,doctor_id):
        return self.repo.find_by_id(doctor_id)

    def find_by_family_and_specialty(self, family, specialty):
        return self.repo.find_by(and_(Doctor.family.like(family + "%"), Doctor.specialty.like(specialty + "%")))