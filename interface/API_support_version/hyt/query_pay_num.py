#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

import pymysql

def query_pay(pay_num):
    conn= pymysql.connect(host='192.168.0.105', port=3306, user='root', passwd='hyt@root@123',db='hyt_ecshop')
    cur = conn.cursor()
    cur.execute("select o.payOrderNum,o.total_price from kqecshop_ordermain o WHERE o.num = %s ;" % pay_num )
    result = cur.fetchall()
    pay_num = result[0][0]
    pay_mon = int(result[0][1] * 100)       #转化为int
    #print (pay_num,pay_mon)
    return (result[0][0],result[0][1])      #返回订单，支付金额

if __name__ == '__main__':
   list = query_pay(18699)
   print (list)