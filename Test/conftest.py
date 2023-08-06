import pytest
from selene import browser
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def brwsr_cnfg():
    # options = webdriver.ChromeOptions()
    # options.headless = True
    # browser.config.driver = webdriver.Chrome(options)
    browser.config.window_width = 1900
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'