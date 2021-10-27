# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from common.base import Base

class homepage(Base):
    # 首页,homepage:权限框元素及方法,该类继承自BasePage类

    # 授权框-》允许 按钮
    allow_button = (By.ID, 'com.android.permissioncontroller:id/permission_allow_button')

    # 授权框-》拒绝 按钮
    deny_button = (By.ID, 'com.android.permissioncontroller:id/permission_deny_button')

    # 授权框-》文案 按钮
    authority_text = (By.ID, 'com.android.permissioncontroller:id/permission_message')

    # 点击 授权框-》允许 按钮
    def click_authority_allow_button(self):
        self.driver.find_element(*self.allow_button).click()
