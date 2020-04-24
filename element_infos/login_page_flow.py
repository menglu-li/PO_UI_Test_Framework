import os
from selenium import webdriver
from selenium.webdriver.common.by import By
# 并把各种输入点击操作写入日志

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')

class LoginPage():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://127.0.0.1/biz/user-login-L2Jpei8=.html')
        self.username_inputbox = self.driver.find_element(By.ID, 'account') # 属性--》控件
        self.password_inputbox = self.driver.find_element(By.NAME, 'password')
        self.keeplogin_checkbox = self.driver.find_element(By.ID, 'keepLoginon')
        self.login_button = self.driver.find_element(By.ID, 'submit')

    def input_username(self, username): #方法--》控件的操作
        self.username_inputbox.send_keys(username)

    def input_password(self, password):
        self.password_inputbox.send_keys(password)

    def click_keeplogin(self):
        self.keeplogin_checkbox.click()

    def click_login(self):
        self.login_button.click()


if  __name__ =='__main__':
    login_page = LoginPage()
    login_page.input_username('admin')
    login_page.input_password('admin123456')
    login_page.click_keeplogin()
    login_page.click_login()


