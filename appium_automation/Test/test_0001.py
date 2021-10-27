# -*- coding:utf-8 -*-

from Page.AuthorityPage import AuthorityPage
import allure
from Basic import driver

@allure.feature('【权限授权】模块')  #主要功能模块
@allure.story('允许授权')  #分支功能
@allure.issue('https://www.baidu.com/')#添加缺陷对应链接
@allure.testcase('https://www.baidu.com/')#添加用例对应链接

class Test_Authority(object):
    # 对象初始化
    a_driver = driver.init_driver()
    authority = AuthorityPage(a_driver)

    @allure.title('用例1：允许授权后取消授权')  # 用例标题
    @allure.severity('blocker')  # 用例级别
    def test_01(self):
        """
                这里是允许授权功能的测试用例
                :return:
        """
        try:
            with allure.step('第一步：点击允许授权'):  # 用例步骤
                allure.attach('允许', '按钮')  # attach可以打印一些附加信息
                self.authority.click_authority_allow_button() #授权框点击允许按钮

                allure.attach('点击成功', '期望结果')
                assert self.authority.authority_text

            with allure.step('第二步：点击取消授权'):  # 用例步骤
                allure.attach('取消', '按钮')  # attach可以打印一些附加信息
                self.authority.click_authority_deny_button()  # 授权框点击取消按钮

                assert self.authority.authority_text
        except Exception as E:
            allure.attach('点击失败', '实际结果')
            self.authority.take_screenShot()
        finally:
            self.authority.take_screenShot()

    @allure.title('用例2：取消授权')  # 用例标题
    @allure.severity('blocker')  # 用例级别
    def test_02(self):
        try:
            with allure.step('第一步：取消授权'):  # 用例步骤
                allure.attach('允许', '按钮')  # attach可以打印一些附加信息
                self.authority.click_authority_deny_button()  # 授权框点击允许按钮
                assert self.authority.authority_text
        except Exception as E:
            self.authority.take_screenShot()

