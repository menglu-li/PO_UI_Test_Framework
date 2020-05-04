import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.browser import Browser
from common.excel_element_info_utils import ExcelElementinfoUtil
import time

# 并把各种输入点击操作写入日志

# current_path = os.path.dirname(__file__)
# driver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.implicitly_wait(10)
        # self.driver.get('http://127.0.0.1/biz/user-login-L2Jpei8=.html')
        # self.username_inputbox = {'element_name':'用户输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value':'//input[@id="account"]',
        #                           'timeout':5}
        # self.password_inputbox = {'element_name':'密码输入框',
        #                                   'locator_type': 'xpath',
        #                                   'locator_value':'//input[@name="password"]',
        #                                   'timeout':5}
        # self.keeplogin_checkbox = {'element_name': '保持登录',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//input[@id="keepLoginon"]',
        #                           'timeout': 5}
        # self.login_button = {'element_name': '登录',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//button[@id="submit"]',
        #                           'timeout': 5}
        self.element_info = ExcelElementinfoUtil('login_page').get_element_info()
        self.username_inputbox = self.element_info['username_inputbox']
        self.password_inputbox = self.element_info['password_inputbox']
        self.keeplogin_checkbox = self.element_info['keeplogin_checkbox']
        self.login_button = self.element_info['login_button']

    def input_username(self, username):
        self.input(self.username_inputbox, username)

    def input_password(self, password):
        self.input(self.password_inputbox, password)

    def click_keeplogin(self):
        self.click(self.keeplogin_checkbox)

    def click_login(self):
        self.click(self.login_button)


if  __name__ =='__main__':
    # webdriver = webdriver.Chrome()
    # login_page = LoginPage(webdriver)
    # webdriver.get('http://127.0.0.1/biz/user-login.html')
    # login_page.set_browser_max()
    # time.sleep(3)
    # login_page.input_username('admin')
    # login_page.input_password('admin123456')
    # login_page.click_keeplogin()
    # login_page.click_login()

    # driver = Browser().get_chrome() # 调用二次封装chromedriver
    driver = Browser().get_driver() # 调用二次封装的driver，根据配置改浏览器
    login_page = LoginPage(driver)
    login_page.open_url('http://127.0.0.1/biz/user-login.html')
    login_page.set_browser_max()
    time.sleep(3)
    login_page.input_username('admin')
    login_page.input_password('admin123456')
    login_page.click_keeplogin()
    login_page.click_login()


