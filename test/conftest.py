from pathlib import Path
import test
import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def brwsr_cnfg():
    browser.config.window_width = 1900
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'


def path(image):
    return str(Path(test.__file__).parent.joinpath(f'{image}').absolute())
