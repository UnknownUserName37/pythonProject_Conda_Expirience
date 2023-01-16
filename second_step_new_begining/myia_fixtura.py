import pytest
from selenium import webdriver


@pytest.fixture()
def test_testo():
    driver = webdriver.Chrome

    driver.quit()
