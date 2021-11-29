# -- coding: utf-8 --
from appium.webdriver.common.mobileby import MobileBy

# app4弹出框
msg_locator=(MobileBy.ID, "android:id/message") # 信息文本
cancel_locator=(MobileBy.ID, "android:id/button2") # 取消
ok_locator=(MobileBy.ID, "android:id/button1") # 确定