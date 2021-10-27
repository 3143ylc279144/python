# -*- coding:utf-8 -*-
import xlrd
def get_exceldata(sheetname,casename):
    reslist=[]
    exceldir = '../data/时钟测试用例.xls'
    workbook=xlrd.open_workbook(exceldir,formatting_info=True)
    worksheet=workbook.sheet_by_name(sheetname)
    idx = 0
    for one in worksheet.col_values(0):
        if casename in one:
            city = worksheet.cell(idx,3).value
            reslist.append(city)
        idx += 1
    return reslist

print(get_exceldata('添加时钟','addcitytime'))