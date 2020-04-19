# 封闭浏览器 并把浏览器操作写入日志

from common.log_utils import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 打开、最大化、最小化，浏览器二次封装
class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')

    def close_browser(self):
        self.driver.close()

    # 元素操作的封装 配合Login_page2使用
    # element_info {'element_name':'用户输入框',
    #                                   'locator_type': 'xpath',
    #                                   'locator_value':'//input[@id=account]',
    #                                   'timeout':5}
    def find_element(self, element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name =='id':
            locator_type= By.ID
        elif locator_type_name =='name':
            locator_type = By.NAME
        elif locator_type_name =='class':
            locator_type = By.CLASS_NAME
        elif locator_type_name =='xpath':
            locator_type = By.XPATH
        element = WebDriverWait(self.driver,locator_timeout)\
            .until(lambda driver: driver.find_element(locator_type,locator_value_info))
        logger.info('[%s]元素识别成功'%element_info['element_name'])
        return element

        # element = WebDriverWait(self.driver,locator_timeout)\
        #     .util(EC.presence_of_element_located(locator_type, locator_value_info)

    def click(self,element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('[%s]元素进行点击成功' % element_info['element_name'])

    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入成功' % element_info['element_name'])

