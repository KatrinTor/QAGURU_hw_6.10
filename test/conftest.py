import os

import pytest
from selene import browser
from selene.support import webdriver


@pytest.fixture(scope='function', autouse=True)
def brwsr_cnfg():
    # driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver.exe')
    browser.config.window_width = 1900
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'

RES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resources'))