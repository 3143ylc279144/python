# -*- coding:utf-8 -*-
import os
import shutil
import subprocess
import time
import pytest
from Basic import Log

# 清空app缓存数据
# os.system("adb shell pm clear com.baoneng.appstore")

# 给虚拟机设置网络
# os.system("adb shell setprop net.dns1 192.168.1.1")

# 判断测试结果数据所在目录是否存在日志，有则删除日志
# file = 'allure-result'
# files = os.listdir(file)
# for i in files:
#     if i.endswith(".json"):
#         os.remove(os.path.join(file + '//' +i))


PATH = os.path.split(os.path.realpath(__file__))[0]
xml_report_path = PATH + "/result/xml"
html_report_path = PATH + "/report/html"
tm = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))


def invoke(md):
    output, errors = subprocess.Popen(md, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o

if __name__ == '__main__':
    # # 执行用例
    # args = '--alluredir=result/'
    # pytest.main(['-s','-v','/Users/yanglicong/pythonProject/appium_automation/testcase',args])
    #
    # #生成html allure generate 测试结果数据所在目录 -o 测试报告保存的目录 --clean
    # os.system("allure generate result/ -o report/ --clean")
    # # 默认浏览器打开测试报告
    # os.system("allure open report")

    log = Log.MyLog()
    log.info("-----------------------------START: %s----------------------------------" % tm)
    shutil.rmtree(xml_report_path)
    args = ['-s', '-v', '/Users/yanglicong/pythonProject/appium_automation/Test', '--alluredir', xml_report_path]
    pytest.main(args)
    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    invoke(cmd)
    log.info("-----------------------------END: %s------------------------------------" % tm)
    os.system("allure open report/html")

