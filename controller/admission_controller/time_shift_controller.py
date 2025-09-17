from model.entity.admission.time_shift import TimeShift
from model.service.admission_service.time_shift_sevice import TimeShiftService
from model.tools.decorators import exception_handling


class TimeShiftController:
    def __init__(self):
        self.service = TimeShiftService()

    @exception_handling
    def save(self,start_time,end_time,day_of_week,room_number,doctor_id):
        time_shift = TimeShift(start_time,end_time,day_of_week,room_number,doctor_id)
        return self.service.save(time_shift)

    @exception_handling
    def edit(self,shift_id,start_time,end_time,day_of_week,room_number,doctor_id):
        time_shift = TimeShift(start_time,end_time,day_of_week,room_number,doctor_id)
        time_shift.shift_id = shift_id
        return self.service.edit(time_shift)

    @exception_handling
    def delete(self,shift_id):
        return self.service.delete(shift_id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_id(self,shift_id):
        time_shift = self.service.find_by_id(shift_id)
        return time_shift

    @exception_handling
    def find_by_day_of_week_and_doctor_id(self, day_of_week, doctor_id):
        return self.service.find_by_day_of_week_and_doctor_id(day_of_week, doctor_id)