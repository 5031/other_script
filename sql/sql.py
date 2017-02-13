#!/usr/bin/env python
#_*_ coding=utf-8 _*_
#Date:2016-12-28 PASS
_author_ = 'wenzhe'

import pymysql
import configparser
import os,time
timer = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def sql_operate(pay_num):
    conn= pymysql.connect(host='192.168.0.105', port=3306, user='root', passwd='hyt@root@123',db='hyt_ecshop')
    cur = conn.cursor()
    cur.execute(pay_num )
    result = cur.fetchall()
    pay_num = result[0][0]
    return (result[0][0],result[0][1])      #返回订单，支付金额

if __name__ =='__main__':

    list = sql_operate("select o.payOrderNum,o.total_price from kqecshop_ordermain o WHERE o.num = %s ;" % 11357 )  #直接传入要操作的sql语句即可
    print (list)
    #print (type(host),host)