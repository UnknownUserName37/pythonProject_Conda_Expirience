import pytest


def test_testt(test_testo):
    driver = test_testo
    driver.get("https:/the-internet.herokuapp.com/login")
    elem_id = driver.find_element_by_id('username')
    print(elem_id)
    elem_name = driver.find_element_by_name('username')