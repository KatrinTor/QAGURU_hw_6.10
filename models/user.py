import datetime
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    subjects: str
    date_of_birth: datetime.date
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str
