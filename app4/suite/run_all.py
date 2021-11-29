# -- coding: utf-8 --
from app4.utils.HTMLTestRunner import HTMLTestRunner
import unittest

# 批量运行testcase包里所有测试用例文件，写入html格式的测试报告文件中
if __name__ == '__main__':
    testsuite1=unittest.defaultTestLoader.discover("../testcase","case*.py")
    with open("../report/test_result.html","wb") as file1:
        runner1=HTMLTestRunner(file1,verbosity=2,title="AppiumTestResult",description="The following is appium test summary:")
        runner1.run(testsuite1)