from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromOptions
import chromedriver_binary

def run_script():

    options = ChromOptions()
    driver = Chrome(options=options)
    driver.get("https://skillbox.ru")
    driver.quit()

if __name__ == "__main__" :

    run_script()

