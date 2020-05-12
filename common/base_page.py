# 封闭浏览器 并把浏览器操作写入日志

import time
from common.log_utils import *
from common.config_until import *
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

    # 输入框
    def input(self,element_info,content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入成功' % element_info['element_name'])

    # 滚动到元素
    def scroll_to_element(self, element_info):
        self.driver.execute_script("arguments[0].scrollIntoView()",self.find_element(element_info))

    # 移动到元素
    def move_to_element(self, element_info):
        webdriver.ActionChains(self.driver).move_to_element(element_info).perform()

    # 长按元素
    def long_press_element(self, element_info, second):
        webdriver.ActionChains(self.driver).click_and_hold(element_info).pause(second).release().perform()

    # 跳转到frame
    def switch_to_frame(self, element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    # 跳转到frame
    def switch_to_frame_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)

    # 跳转到frame
    def switch_to_frame_any(self,**element_info):
        if 'id' in element_info.keys():
            self.driver.switch_to.frame(element_info['id'])
        elif 'name' in element_info.keys():
            self.driver.switch_to.frame(element_info['name'])
        # element_info 是个对象 switch_to_frame(id=elelement_info)
        elif 'element' in element_info.keys():
            element = self.find_element(element_info)
            self.driver.switch_to.frame(element)

    # 键盘tab
    def send_keys_tab(self,element_info):
        self.find_element(element_info).send_key(Keys.TAB)

    # 键盘ctrl+a
    def send_keys_ctrla(self, element_info):
        self.find_element(element_info).send_key(Keys.CONTROL,'a')

    # 键盘ctrl+c
    def send_keys_ctrlc(self, element_info):
        self.find_element(element_info).send_key(Keys.CONTROL,'c')

    # 键盘ctrl+v
    def send_keys_ctrlv(self, element_info):
        self.find_element(element_info).send_key(Keys.CONTROL,'v')

    # selenium 执行js
    # def execute_script(self,js_str,element_info=None):
    #     if element_info:
    #         self.driver.execution_script(js_str)
    #     else:
    #         self.driver.execute_script(js_str, None)


    # 执行js
    def excute_js(self,js_str,element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str, element_info)

    # 删除元素属性
    def delete_attribute_value(self, element_info, attribute_name, value):
        element = self.driver.find_element(element_info)
        js_scripts = 'arguments[0].removeAttribute("%s");'%attribute_name
        self.driver.execute_script(js_scripts, element)

    # 修改元素属性
    def update_attribute_value(self, element_info, attribute_name, value):
        element = self.driver.find_element(element_info)
        js_scripts = 'arguments[0].setAttribute("%s,%s");'%attribute_name %value
        self.driver.execute_script(js_scripts, element)

    # 弹出窗封装
    # def switch_to_alert(self, action = 'accept', time_out = local_config.time_out):
    def switch_to_alert(self, action = 'accept', time_out = 5):
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert()
        alert_text = alert.text
        if action == 'accept':
            alert.accept()
        elif action == 'dismiss':
            alert.dismiss()
        return alert_text

    # 获取当前窗口句柄
    def get_windows_handle(self):
        return self.driver.current_window_handle()

    # 切换到窗口句柄
    def switch_window_handle(self,window_handle):
        return self.driver.switch_to.window(window_handle)

    # 获取窗口名称
    def get_title(self):
        return self.driver.title

    # 获取窗口地址
    def get_url(self):
        return self.driver.current_url

    # 按名称切换窗口
    def swith_to_windows_by_title(self,title):
        window_handles = self.driver.window_handles
        for window_handle  in window_handles:
            # if self.get_title == title:
            if WebDriverWait(self.driver, local_config.time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break

    # 按url切换窗口
    def swith_to_windows_by_url(self,url):
        window_handles = self.driver.window_handles
        for window_handle  in window_handles:
            # if self.get_url == url:
            if WebDriverWait(self.driver, local_config.time_out).until(EC.title_contains(url)):
                self.driver.switch_to.window(window_handle)
                break

    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        return current_time

    # 保存截个图
    def save_screenshot(self):
        screenshot_path = self.get_current_time()+'.png'
        webdriver.save_screenshot(screenshot_path)
        return screenshot_path

    # 老师==保存截图
    # def screenshot_as_file(self, *screenshot_path): #*screenshot_path不传值用默认，传值就用拼接地址
    #     if len(screenshot_path) == 0:
    #         screenshot_filepath = local_config.get_screenshot_url()
    #     else:
    #         screenshot_filepath =screenshot_path[0]
    #     now = time.strftime('%Y-%m-%d %H-%M-%S')
    #     screenshot_filepath = os.path.join(current_dir, screenshot_path, 'UITest')
    #     self.driver.get_screenshot_as_file(screenshot_filepath)









