# -- coding: utf-8 --
from selenium.common.exceptions import NoSuchElementException

# 网页里最基本的操作
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def locate(self,locator):
        element=None
        try:
            element=self.driver.find_element(*locator)
        except NoSuchElementException as e:
            print(e)
        return element

    def click(self,locator):
        self.locate(locator).click()

    def clear(self,locator):
        self.locate(locator).clear()

    def input(self,locator,txt):
        self.locate(locator).send_keys(txt)

    def clear_and_input(self,locator,txt):
        self.clear(locator)
        self.input(locator,txt)

    def get_text(self,locator):
        return self.locate(locator).text

    def get_attribute(self,locator,attribute_name):
        return self.locate(locator).get_attribute(attribute_name)