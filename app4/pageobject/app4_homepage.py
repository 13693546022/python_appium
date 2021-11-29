# -- coding: utf-8 --
from app4.locator import app4_homepage_locator
from app4.base.pagebase import BasePage

# 主页操作
class HomePage(BasePage):
    def input_num1(self,n1): # 输入加数一
        self.clear_and_input(app4_homepage_locator.num1_locator,n1)

    def input_num2(self,n2): # 输入加数二
        self.clear_and_input(app4_homepage_locator.num2_locator,n2)

    def click_add(self): # 点击计算
        self.click(app4_homepage_locator.add_locator)

    def click_reset(self): # 点击重置
        self.click(app4_homepage_locator.reset_locator)

    def click_exit(self): # 点击退出
        self.click(app4_homepage_locator.exit_locator)

    def get_result(self): # 获得结果文本框的值
        return self.get_text(app4_homepage_locator.result_locator)

    def get_msg(self): # 获得红色提示信息的文本
        return self.get_text(app4_homepage_locator.msg_locator)

    def input_all(self,n1,n2): # 输入加数一和加数二
        self.input_num1(n1)
        self.input_num2(n2)

    def add_all(self,n1,n2): # 输入加数一和加数二，计算
        self.input_all(n1,n2)
        self.click_add()

    def reset_all(self,n1,n2): # 输入加数一和加数二，重置
        self.input_all(n1,n2)
        self.click_reset()

    def get_num1(self): # 获得加数一当前内容
        return self.get_text(app4_homepage_locator.num1_locator)

    def get_num2(self): # 获得加数二当前内容
        return self.get_text(app4_homepage_locator.num2_locator)