import enum
from datetime import datetime, time, date

from pydantic import BaseModel, HttpUrl

# example schemas class for your database models

class ScheduleSchema(BaseModel):
    id: int
    user_id: int
    date: date
    time: time

