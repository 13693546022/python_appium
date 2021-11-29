# -- coding: utf-8 --
from appium.webdriver.common.mobileby import MobileBy

# app4主页
num1_locator=(MobileBy.ID, "num1") # 加数一
num2_locator=(MobileBy.ID, "num2") # 加数二
add_locator=(MobileBy.ID, "button1") # 计算
reset_locator=(MobileBy.ID, "button2") # 重置
exit_locator=(MobileBy.ID, "button3") # 退出
result_locator=(MobileBy.ID, "result") # 结果
msg_locator=(MobileBy.ID, "info") # 红色提示信息

