import datetime

from QAGURU_hw_6_10.models.user import User
from QAGURU_hw_6_10.pages.registration_page import RegistrationPage


def test_filling_form():
    registration_page = RegistrationPage()

    kat = User(
        first_name='Katrin',
        last_name='Torsunova',
        email='Katrin@test.ru',
        gender='Female',
        phone_number='8967625366',
        date_of_birth=datetime.date(1994, 11, 15),
        hobbies='Reading',
        subjects='Biology',
        picture='trusost.jpg',
        current_address='ul. Kronverksky 49',
        state='Haryana',
        city='Karnal')

    registration_page.open()
    registration_page.register(kat)
    registration_page.should_have_registered(kat)
