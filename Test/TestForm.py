import os

from selene import have
from selene import browser
from PageObject.RegistrationPage import RegistrationPage


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

    # browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    # browser.element('.modal-body').should(have.text('Katrin Torsunova'))
    # browser.element('.modal-body').should(have.text('Katrin@test'))
    # browser.element('.modal-body').should(have.text('Female'))
    # browser.element('.modal-body').should(have.text('8967625366'))
    # browser.element('.modal-body').should(have.text('15 November,1994'))
    # browser.element('.modal-body').should(have.text('Biology'))
    # browser.element('.modal-body').should(have.text('Reading'))
    # #browser.element('.modal-body').should(have.text('photo1687420339.jpeg'))
    # browser.element('.modal-body').should(have.text('ul. Kronverksky 49'))
    # browser.element('.modal-body').should(have.text('Haryana Karnal'))
