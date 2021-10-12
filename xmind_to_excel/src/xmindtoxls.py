# -*- coding:utf-8 -*-
from xmindparser import xmind_to_dict
import re
import xlwt

class xmind_to_xls():
    def xmind_num(self, value):
        """获取xmind标题个数"""
        try:
            return len(value['topics'])
        except KeyError:
            return 0

    def xmind_title(self,value):
        """获取xmind标题内容"""
        return value['title']

    def  xmind_cat(self, filename):
        '''调试函数，打印内容用的'''
        self.out = xmind_to_dict(filename)
        self.story = self.out[0]['topic']['topics']
        self.num = len(self.story)
        print(self.out)
        print(self.out[0]['topic']['title'])
        return self.story, self.num

    def write_excel(self, xmind_file, servicename='', editionname='', performer=''):
        '''生成excel文件函数'''
        self.f = xlwt.Workbook()
        self.sheet1 = self.f.add_sheet('sheet1',cell_overwrite_ok=True)
        self.row0 = ["storyid", '需求名称', '功能模块', '测试用例名称', '前置条件', '执行步骤', '期望结果', '服务名称', '版本', '维护人']
        #生成第一行
        for i in range(0, len(self.row0)):
            self.sheet1.write(0, i, self.row0[i])
        self.out = xmind_to_dict(xmind_file)
        self.xls_name = self.out[0]['topic']['title']
        self.story = self.out[0]['topic']['topics']
        self.storynum = len(self.story)
        j = 1  # 用例计算器
        z = 0  # 用例结果数计数器
        for i in range(0, self.storynum):
            self.storyname = self.story[i]['title']
            print(self.storyname)
            self.regex_str = ".*[\[【](.+?)[\]】].*"
            self.storyid_reg = re.match(self.regex_str, self.storyname)
            if self.storyid_reg:
                # print(self.storyid_reg) #取出正则解析后的结果
                self.storyid = self.storyid_reg.group(1)#正则取出用例编号
                print(self.storyid_reg.group(1))
            self.testmodel_num = len(self.story[i]['topics'])

            for s in range(0,self.testmodel_num):
                self.modle_name = self.xmind_title(self.story[i]['topics'][s])
                self.testcase_num = self.xmind_num(self.story[i]['topics'][s])
                for k in range(0,self.testcase_num):  #测试用例数
                    self.testcase = self.story[i]['topics'][s]['topics'][k]
                    self.testcase_name = self.xmind_title(self.testcase)
                    self.testcase_stepnum = self.xmind_num(self.testcase) #每个用例的步骤数量
                    self.testcase_condition = self.xmind_title(self.testcase['topics'][0])  # 用例预置条件
                    self.sheet1.write(s+k + i + z + j, 0, self.storyid)
                    self.sheet1.write(s+k + i + z + j, 1, self.storyname)
                    self.sheet1.write(s+k + i + z + j, 2, self.modle_name)
                    self.sheet1.write(s+k + i + z + j, 3, self.testcase_name)
                    self.sheet1.write(s+k + i + z + j, 4, self.testcase_condition)
                    self.sheet1.write(s+k + i + z + j, 7, servicename)
                    self.sheet1.write(s+k + i + z + j, 8, editionname)
                    self.sheet1.write(s+k + i + z + j, 9, performer)
                    for x in range(1,self.testcase_stepnum):  #测试用例步骤数
                        self.testcase_step = self.testcase['topics'][x]
                        self.teststep_title = self.xmind_title(self.testcase_step) #用例步骤名称
                        self.teststep_num = self.xmind_num(self.testcase_step) #用例步骤个数
                        if self.teststep_num != 0:
                            for y in range(0, self.teststep_num):
                                self.test_results = self.testcase_step['topics'][y]
                                self.test_result = self.xmind_title(self.test_results)#用例结果
                                self.sheet1.write(s+k + i + z + j+y, 5, self.teststep_title)
                                self.sheet1.write(s+k + i + z + j+y, 6, self.test_result)
                            z = z+y+1
                        else:
                            self.test_result = '/'
                            self.sheet1.write(s+k + i + z + j, 5, self.teststep_title)
                            self.sheet1.write(s+k + i + z + j, 6, self.test_result)
                            # z = z
            j=j+k
        self.f.save(self.xls_name+'.xls') #xls名称取xmind主题名称

if __name__ == '__main__':
     xmind_file = "Y:/Documents/软件/软件/xmind_to_excel/xmind模板.xmind"  # xmind文件
     servicename = 'aa'  #服务名称
     editionname = 'bb'  #版本
     performer = 'cc'  #执行人员
     xmind_to_xls().write_excel(xmind_file, servicename, editionname, performer)
     xmind_to_xls().xmind_cat(xmind_file)