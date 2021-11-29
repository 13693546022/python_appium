import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

# 基类：让它作为测试用例类的父类
class MyCaseBase(unittest.TestCase):
    def setUp(self) -> None:
        desired_capabilities={
            "platformName":"Android",
            "platformVersion":"8.0",
            "deviceName":"192.168.206.101:5555",
            "app":r"D:\Apks\app4-debug.apk",
            "appPackage":"com.example.app4",
            "appActivity":".MainActivity",
            "unicodeKeyboard":True,
            "resetKeyboard":True,
            "noSign":True,
            "noReset":True
        }

        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.quit()

    def is_element_present(self,locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
