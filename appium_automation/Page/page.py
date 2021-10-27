# -*- coding:utf-8 -*-
class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def initloginpage(self):
        return Login_Page(self.driver)
