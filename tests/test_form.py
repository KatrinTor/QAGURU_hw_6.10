import os

from pages.resourses import RegistrationPage
from conftest import RES_DIR

def test_fill_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_full_name('Katrin', 'Torsunova')
    registration_page.fill_email('Katrin@test.ru')
    registration_page.choose_gender('Female')
    registration_page.fill_user_number('8967625366')
    registration_page.fill_birthdate(1994, 'November', 15)
    registration_page.set_subject('B')
    registration_page.select_hobbie('Reading')
    registration_page.attach_file('trusost.jpg')
    registration_page.fill_address('ul. Kronverksky 49')
    registration_page.select_state('Haryana')
    registration_page.select_city('Karnal')
    registration_page.click_submit_batton()

    registration_page.should_have(
        'Katrin Torsunova',
        'Katrin@test.ru',
        'Female',
        '8967625366',
        '15 November,1994',
        'Biology',
        'Reading',
        'trusost.jpg',
        'ul. Kronverksky 49',
        'Haryana Karnal')
