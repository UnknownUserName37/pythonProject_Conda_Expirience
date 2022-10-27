#Remoute Auto_Test #2

from selenium.webdriver import Chrome, Remote

class TestExample: #TestSuit

    def test_test(self): #TestCase

        driver = Remote(desired_capabilities={
            "browserName": "chrome",
            "browserVersion": "latest"
        }, command_executor="http://127.0.0.1:4444/wd/hub")
        driver.get("https://pythonist.ru/top-8-sajtov-s-besplatnymi-kursami-po-python-dlya-nachinayushhih/")

        driver.quit()

