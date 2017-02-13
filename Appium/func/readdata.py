#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
import configparser
import os,xlrd

def readconf(var1,var2):                          #读取配置文件
     current_dir = os.path.dirname(os.path.dirname(__file__))           #通过本文件__file__获取相对路径
     con = configparser.ConfigParser()
     con.read(current_dir + '\\test_machine.conf',encoding='utf-8')
     u = con.get(var1,var2)
     return u

def read_casedata(caseid):                      #读取excel
    current_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    data_path = current_path + '/data/test_caseid.xls'
    data = xlrd.open_workbook(data_path)
    table = data.sheet_by_name('Sheet1')         #获取该excel中指定sheet
    #print (type(table.col_values(0)))             #获取第一列
    #result_table = table.col_values(0)[1:]          #,第二条数据开始
    result_table = table.row_values(caseid)
    return result_table

if __name__ == '__main__':
     # result = readconf('sec','url')
     # print (result)
     #
     testid = 1
     file = read_casedata(testid)
     print(file)
