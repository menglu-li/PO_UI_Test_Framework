from element_infos import login_page
from selenium.webdriver.common.by import By

class MainPage():

    def __init__(self):
        login_page.login_page.input_username('admin')
        login_page.login_page.input_password('password')
        login_page.login_page.click_keeplogin()
        login_page.login_page.click_login()

        self.driver=login_page.login_page.driver
        self.driver.find_element(By.ID, '')

