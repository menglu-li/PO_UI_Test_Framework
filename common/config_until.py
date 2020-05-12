import os
import configparser

current_path=os.path.dirname(__file__)
config_path = os.path.join(current_path, '../conf/config.ini')

class ConfigUtils():
    def __init__(self,conf_path = config_path):
        self.config = configparser.ConfigParser()
        self.config.read(conf_path,encoding='utf-8')

    @property
    def get_test_url(self):
        test_url = self.config.get('default', 'testurl')
        return test_url

    def get_driver_path(self):
        driverpath = self.config.get('default', 'driverpath')
        return driverpath

    # @property
    # def get_chrome_driver(self):
    #     chrome_driver = self.config.get('default', 'chrome_driver')
    #     return chrome_driver
    #
    # @property
    # def get_firefox_driver(self):
    #     firefox_driver = self.config.get('default', 'firefox_driver')
    #     return firefox_driver

    # @property
    def get_init_driver(self):
        init_driver = self.config.get('default', 'init_driver_type')
        return init_driver

    # @property
    def time_out(self):
        time_out = self.config.get('default', 'time_out')
        return time_out

    # @property
    def get_screenshot_url(self):
        screenshot_url = self.config.get('default', 'screenshot_url')
        return screenshot_url

local_config = ConfigUtils()

# if __name__ == '__main__':
#     local_config = ConfigUtils()
#     print(local_config.get_driver_path())
#     print(local_config.get_chrome_driver())
#     print(local_config.get_firefox_driver())
#     print(local_config.get_init_driver())

