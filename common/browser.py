import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.config_until import local_config

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path,'..', local_config.get_driver_path())

class Browser():
    # def __init__(self,driver_path = driver_path):
    def __init__(self, driver_name = local_config.get_init_driver()):
        # self.driver_path = driver_path
        self.driver_name = driver_name

    # 根据配置文件选择默认浏览器类型
    def get_driver(self):
        if self.driver_name.lower() == 'chrome':
            return self.get_chrome()
        elif self.driver_name.lower() =='firefox':
            return self.get_firefox()
        # elif self.driver_name.lower() == 'edge':
        #     return self.get_edge()

    def get_chrome(self):
        chrome_options= Options()
        chrome_options.add_argument('--disable--gpu') # 加上这个属性规避BUG
        chrome_options.add_argument('lang=zh_CN.UTF-8') # 设置浏览器网页默认utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome 受自动化控制条显示
        chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])  # 取消chrome 受自动化控制条显示
        chrome_driver = os.path.join(driver_path, 'chromedriver.exe')
        print(chrome_driver)
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
        return driver

    def get_firefox(self):
        firefox_driver = os.path.join(driver_path, 'geckdriver.exe')
        driver = webdriver.Chrome(executable_path = firefox_driver)
        return driver

    # selenium 分布式grid 远程别人电脑控制浏览器??
    def get_grid(self):
        pass



if __name__=='__main__':
    print(driver_path)
    chrome_driver = os.path.join(driver_path, 'chromedriver.exe')
    print(chrome_driver)
    # Browser.get_chrome()

