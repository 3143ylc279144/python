# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter.filedialog import askopenfilename
from src.xmindtoxls import xmind_to_xls
from tkinter.messagebox import showinfo
import re

# 定义MainUI类表示应用/窗口，继承Frame类
class MainUI(tk.Frame):
    # Application构造函数，master为窗口的父控件
    def __init__(self, master=None):
        # 初始化Application的Frame部分
        tk.Frame.__init__(self, master)
        # 显示窗口，并使用grid布局
        self.grid()
        self.path = tk.StringVar()
        # 创建控件
        self.createWidgets()

    def selectPath(self):
        '''选择要转换成excel的xmind地址'''
        self.path_ = askopenfilename()
        self.path.set(self.path_)

    # 创建控件
    def createWidgets(self):
        '''生成gui界面'''
        # 创建一个标签，输出要显示的内容
        self.firstLabel = tk.Label(self, text="目标路径")
        # 设定使用grid布局
        self.firstLabel.grid(row = 0, column = 0)
        self.firstEntry = tk.Entry(self,textvariable = self.path)
        self.firstEntry.grid(row=0, column=1)
        # 创建一个按钮，用来触发answer方法
        self.clickButton = tk.Button(self, text="路径选择", command=self.selectPath)
        # 设定使用grid布局
        self.clickButton.grid(row = 0, column = 2)
        # 创建一个标签，输入模块
        self.secLabel = tk.Label(self, text="模块")
        # 设定使用grid布局
        self.secLabel.grid(row=1, column=0)
        self.module = tk.StringVar()
        self.secEntry = tk.Entry(self,textvariable = self.module)
        self.secEntry.grid(row=1, column=1)
        # 创建一个标签，输入版本号
        self.trLabel = tk.Label(self, text="版本号")
        # 设定使用grid布局
        self.trLabel.grid(row=2, column=0)
        self.buildnum = tk.StringVar()
        self.trEntry = tk.Entry(self,textvariable = self.buildnum)
        self.trEntry.grid(row=2, column=1)
        # 创建一个标签，输入执行人
        self.fourLabel = tk.Label(self, text="执行人")
        # 设定使用grid布局
        self.fourLabel.grid(row=3, column=0)
        self.owner = tk.StringVar()
        self.fourEntry = tk.Entry(self,textvariable = self.owner)
        self.fourEntry.grid(row=3, column=1)
        # 创建一个提交按钮，用来触发提交方法,获取值
        self.clickButton = tk.Button(self, text="提交",command=self.getvalue)
        # 设定使用grid布局
        self.clickButton.grid(row=4, column=1)

    def getvalue(self):
        '''获取输入的值，并执行转换excel函数'''
        global way,module,buildnum,owner
        way = self.path.get()
        module = self.module.get()
        buildnum = self.buildnum.get()
        owner = self.owner.get()
        print(way,module,buildnum,owner)
        self.regvalue = '.*\.xmind$'
        self.xmind_reg = re.match(self.regvalue,way )
        if self.xmind_reg:
            # xmind转换成xls
            self.xmind_to_xls = xmind_to_xls()
            self.xmind_to_xls.write_excel(way,module,buildnum,owner)
        else:
            showinfo(title='提示',message='请选择正确的xmind文件，谢谢！')

# 创建一个MainUI对象
app = MainUI()
# 设置窗口标题
app.master.title('「xmind转xls」')
# 设置窗体大小
app.master.geometry('400x200')
# 主循环开始
app.mainloop()