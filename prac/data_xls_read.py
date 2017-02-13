#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
import xlrd
import pymysql

def read_casedata(caseid):                      #需要传入测试用例id
    data = xlrd.open_workbook("hyt_pay_data.xls")
    table = data.sheet_by_name('Sheet1')         #获取该excel中指定sheet
    #print (type(table.col_values(0)))             #获取第一列
    #result_table = table.col_values(0)[1:]          #,第二条数据开始
    result_table = table.row_values(caseid)              #获取第二行数据,返回list
    return result_table

if __name__ == '__main__':
    caseid = 1
    file = read_casedata(caseid)
    print (file)

