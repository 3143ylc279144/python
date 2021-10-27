# -*- coding:utf-8 -*-
from selenium import webdriver

# apk参数
def init_driver():
    desired_caps = {}
    # 手机 系统信息
    desired_caps['platformName'] = 'Android'  # 设置平台
    desired_caps['platformVersion'] = '10.0'  # 系统版本
    # 设备号
    desired_caps['deviceName'] = '61359515231666'  # 设备id
    # 包名
    desired_caps['appPackage'] = ''  # 包名
    # 启动名
    desired_caps['appActivity'] = ''  # 启动的activity
    desired_caps['automationName'] = 'Uiautomator2'
    # 允许输入中文
    # desired_caps['unicodeKeyboard'] = True
    # desired_caps['resetKeyboard'] = True
    # desired_caps['autoGrantPermissions'] = True
    desired_caps['noReset'] = False
    # 手机驱动对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver

def driver_weixin():
    desired_caps = {}
    # 手机 系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10.0'
    # 设备号
    desired_caps['deviceName'] = '61359515231666'
    # 包名
    desired_caps['appPackage'] = 'com.tencent.mm'
    # 启动名
    desired_caps['appActivity'] = '.ui.LauncherUI'
    # desired_caps['automationName'] = 'Uiautomator2'
    # 允许输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] = True
    # desired_caps["newCommandTimeout"] = 30
    # desired_caps['fullReset'] = 'false'
    # desired_caps['newCommandTimeout'] = 10
    # desired_caps['recreateChromeDriverSessions'] = True
    desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}
    # 手机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver

# def tearDown(self):
#     self.driver.quit() #case执行完退出
