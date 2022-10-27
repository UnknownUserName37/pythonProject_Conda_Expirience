from selenium.webdriver.common.by import By
from selenium import webdriver
class testim_free:
    def find_object_for_test(self, Chrome):
        driver = Chrome
        driver.get("https://the-internet.herokuapp.com/login")

        elem_text = driver.find_element(By.ID, "username")

        pass

