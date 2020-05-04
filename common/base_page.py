# 封闭浏览器 并把浏览器操作写入日志

from common.log_utils import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# 打开、最大化、最小化，浏览器二次封装
class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def open_url(self,url):
        self.driver.get(url)

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

    def double_click(self,element_info):
        element = self.find_element(element_info)
        element.double.click()
        logger.info('[%s]元素进行点击成功' % element_info['element_name'])

    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入成功' % element_info['element_name'])

    def scroll_to_element(self, element_info):
        self.driver.execute_script("arguments[0].scrollIntoView()",self.find_element(element_info))

    def move_to_element(self, element_info):
        webdriver.ActionChains(self.driver).move_to_element(element_info)

    def switch_to_frame(self, element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    def switch_to_frame_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)

    def switch_to_frame_any(self,**element_info):
        if 'id' in element_info.keys():
            self.driver.switch_to.frame(element_info['id'])
        elif 'name' in element_info.keys():
            self.driver.switch_to.frame(element_info['name'])
        # element_info 是个对象 switch_to_frame(id=elelement_info)
        elif 'element' in element_info.keys():
            element = self.find_element(element_info)
            self.driver.switch_to.frame(element)

    def send_keys_tab(self,element_info):
        self.find_element(element_info).send_key(Keys.TAB)

    def send_keys_ctrla(self, element_info):
        self.find_element(element_info).send_key(Keys.CONTROL,'a')

    def send_keys_ctrlc(self, element_info):
        self.find_element(element_info).send_key(Keys.CONTROL,'c')

    def send_keys_ctrlv(self, element_info):
        self.find_element(element_info).send_key(Keys.CONTROL,'v')

    # selenium 执行js
    # def execute_script(self,js_str,element_info=None):
    #     if element_info:
    #         self.driver.execution_script(js_str)
    #     else:
    #         self.driver.execute_script(js_str, None)

    def delete_attribute_value(self, element_info, attribute_name, value):
        element = self.driver.find_element(element_info)
        js_scripts = 'arguments[0].removeAttribute("%s");'%attribute_name
        self.driver.execute_script(js_scripts, element)

    def upbate_attribute_value(self, element_info, attribute_name, value):
        element = self.driver.find_element(element_info)
        js_scripts = 'arguments[0].setAttribute("%s,%s");'%attribute_name %value
        self.driver.execute_script(js_scripts, element)







