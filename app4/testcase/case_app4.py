import unittest
from app4.base.mybase import MyCaseBase
from app4.utils.read_csv import CSVUtil
from ddt import ddt,data,unpack
from app4.pageobject.app4_homepage import HomePage
from app4.pageobject.app4_dialogpage import DialogPage
from app4.locator.app4_homepage_locator import msg_locator
from app4.locator.app4_dialogpage_locator import cancel_locator

all_data=CSVUtil("../testdata/testdata.csv").list_data() # [['TC001','30','50','80'],['TC002','0','99','99']]

@ddt()
class MyTestCase(MyCaseBase):
    @data(*all_data)
    @unpack
    def test_app4(self,tcid,n1,n2,expected):
        print(tcid,n1,n2,expected)
        hp=HomePage(self.driver)
        dp=DialogPage(self.driver)

        if tcid !="TC011": # TC011不输入任何加数，直接退出
            # 输入数据，计算
            hp.add_all(n1,n2)
            if tcid in ["TC001","TC002","TC003","TC008","TC009"]:
                if tcid in ["TC008","TC009"]: # 重置
                    hp.click_reset()
                # 检查实际结果是否等于预期值
                actual_result=hp.get_result()
                self.assertEqual(expected,actual_result)
                if tcid in ["TC008","TC009"]: # 重置
                    # 检查重置后加数一和加数二文本框为空
                    actual_num1=hp.get_num1()
                    self.assertEqual(expected,actual_num1)
                    actual_num2=hp.get_num2()
                    self.assertEqual(expected,actual_num2)
                    if tcid=="TC009":
                        # 检查红色信息消失
                        self.assertFalse(self.is_element_present(msg_locator))
            elif tcid in ["TC004","TC005","TC006","TC007"]:
                # 检查红色信息出现
                self.assertTrue(self.is_element_present(msg_locator))
                # 检查红色提示信息内容等于预期值
                actual_msg=hp.get_msg()
                self.assertEqual(expected,actual_msg)
            else: # “TC010”---取消退出
                # 点击“退出”
                hp.click_exit()
                # 检查弹出信息框（取消出现）
                self.assertTrue(self.is_element_present(cancel_locator))
                # 获得弹出框里的文本进行检查
                actual_msg=dp.get_msg()
                self.assertEqual("是否确认退出？", actual_msg)
                # 点击“取消”
                dp.click_cancel()
                # 检查弹出框消失（取消消失）
                self.assertFalse(self.is_element_present(cancel_locator))
                # 检查app还在前台运行
                s10=self.driver.query_app_state("com.example.app4")
                self.assertEqual(4,s10) # 4代表已在前台运行（显示在界面最上层）
                # 检查三个文本框里的数据仍然显示（没有消失）
                actual_n1=hp.get_num1()
                self.assertEqual(n1,actual_n1)
                actual_n2=hp.get_num2()
                self.assertEqual(n2,actual_n2)
                actual_result=hp.get_result()
                self.assertEqual(expected,actual_result)
        else: # “TC011”---确定退出
            # 点击”退出“
            hp.click_exit()
            # 检查弹出信息框（取消出现）
            self.assertTrue(self.is_element_present(cancel_locator))
            # 获得弹出框里的文本来进行检查
            actual_msg=dp.get_msg()
            self.assertEqual("是否确认退出？",actual_msg)
            # 点击“确定”
            dp.click_ok()
            # 检查app被关闭
            s11=self.driver.query_app_state("com.example.app4")
            self.assertEqual(1,s11) # 1代表已安装未运行

if __name__ == '__main__':
    unittest.main()
