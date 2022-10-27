# Remoute Auto_Test #2

from selenium.webdriver import Remote
import pytest


@pytest.fixture()
def test_test():
    driver = Remote(desired_capabilities={
        "browserName": "chrome",
        "browserVersion": "latest"
    }, command_executor="http://127.0.0.1:4444/wd/hub")
    yield driver
    driver.quit()

