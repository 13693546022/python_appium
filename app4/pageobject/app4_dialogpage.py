# -- coding: utf-8 --
from app4.locator import app4_dialogpage_locator
from app4.base.pagebase import BasePage

# 弹出框的界面操作
class DialogPage(BasePage):
    def get_msg(self): # 获得提示框里的信息
        return self.get_text(app4_dialogpage_locator.msg_locator)

    def click_cancel(self): # 点击取消
        self.click(app4_dialogpage_locator.cancel_locator)

    def click_ok(self): # 点击确定
        self.click(app4_dialogpage_locator.ok_locator)