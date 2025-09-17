from model.entity.admission.time_shift import TimeShift
from model.repository.repository import Repository

class TimeShiftService:
    def __init__(self):
        self.repo = Repository(TimeShift)

    def save(self,time_shift):
        return self.repo.save(time_shift)

    def edit(self,time_shift):
        return self.repo.edit(time_shift)

    def delete(self,shift_id):
        return self.repo.delete(shift_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,shift_id):
        return self.repo.find_by_id(shift_id)

    def find_by_day_of_week_and_doctor_id(self, day_of_week, doctor_id):
        return self.repo.find_by(and_(TimeShift.day_of_week.like(day_of_week + "%"), TimeShift.doctor_id.like(doctor_id + "%")))