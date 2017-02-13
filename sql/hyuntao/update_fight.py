#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

import pymysql

def order_status(order_num):
    '''修改订单状态为已发货'''
    conn = pymysql.connect(host='192.168.0.105', port=3306, user='root', passwd='hyt@root@123',db='hyt_ecshop')     #设置连接
    cur = conn.cursor()
    cur.execute("UPDATE kqecshop_orderform  SET order_status = 30 where order_id = 174281;" )
    for i in cur.fetchall():
        print (i)
        print ('>>>>>>>>>>>>>>>>>>>')
    conn.close()


if __name__ == '__main__':
    order_status(17428)