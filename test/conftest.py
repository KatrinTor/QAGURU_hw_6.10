import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def brwsr_cnfg():
    browser.config.window_width = 1900
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'