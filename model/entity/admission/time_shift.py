from sqlalchemy import Integer, String, Column, Foreignkey
from model.entity.base import Base
from model.entity.admission.doctor import Doctor

class TimeShift(Base):
    __tablename__ = "time_shift"

    shift_id = Column(Integer, primary_key=True, autoincrement=True)
    start_time = Column(String(30), nullable=False)
    end_time = Column(String(30), nullable=False)
    day_of_week = Column(String(30), nullable=False)
    room_number = Column(Integer)
    doctor_id = Column(Integer,Foreignkey("Doctor.doctor_id"), nullable=False)

    def __init__(self, start_time, end_time, day_of_week, room_number, doctor_id):
        self.start_time = start_time
        self.end_time = end_time
        self.day_of_week = day_of_week
        self.room_number = room_number
        self.doctor_id = doctor_id

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.shift_id, self.start_time, self.end_time, self.day_of_week, self.room_number, self.doctor_id))