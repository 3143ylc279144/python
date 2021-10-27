# -*- coding:utf-8 -*-
from appium.webdriver.common import mobileby
from Basic.base import Base

class AuthorityPage(Base):
    # 欢迎页面,authority:权限框元素及方法,该类继承自BasePage类
    by = mobileby.MobileBy()

    # 授权框-》允许 按钮
    allow_button = (by.ID, 'com.android.permissioncontroller:id/permission_allow_button')

    # 授权框-》拒绝 按钮
    deny_button = (by.ID, 'com.android.permissioncontroller:id/permission_deny_button')

    # 授权框-》文案 按钮
    authority_text = (by.ID, 'com.android.permissioncontroller:id/permission_message')

    # 点击 授权框-》允许 按钮
    def click_authority_allow_button(self):
        self.driver.find_element(*self.allow_button).click()

    # 点击 授权框-》取消 按钮
    def click_authority_deny_button(self):
        self.driver.find_element(*self.deny_button).click()

    # 验证授权框文案
    def check_authority_text(self,text):
        self.driver.find_element(*self.authority_text).text()

