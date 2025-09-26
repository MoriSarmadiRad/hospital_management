from model.entity.admission.visit import Visit
from model.repository.repository import Repository


class VisitService :
    def __init__(self):
        self.repo = Repository(Visit)

    def save(self, visit):
        return self.repo.save(visit)

    def edit(self, visit):
        return self.repo.edit(visit)

    def delete(self,visit_id):
        return self.repo.delete(visit_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,visit_id):
        return self.repo.find_by_id(visit_id)

    def find_by_user_id_and_doctor_id(self, user_id, doctor_id):
        return self.repo.find_by(and_(Visit.user_id.like(user_id + "%"), Visit.doctor_id.like(doctor_id + "%")))


