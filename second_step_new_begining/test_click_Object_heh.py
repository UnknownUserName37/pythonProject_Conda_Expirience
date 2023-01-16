#Second_file_for_Auto_Test

def test_set_up_browser(set_up_browser):  # Taste Case
    driver = set_up_browser
    driver.get("https:/the-internet.herokuapp.com/login")
    elem_id = driver.find_element_by_id('username')
    elem_name = driver.find_element_by_name('username')

    
