#!/usr/bin/env python
#_*_ coding=utf-8 _*_
#Staus :2016-12-21 PASS
_author_ = 'wenzhe'


import pymysql
conn = pymysql.connect(host='192.168.0.105', port=3306, user='root', passwd='hyt@root@123',db='hyt_ecshop')     #设置连接
cur = conn.cursor()                                                                                                     #创建一个连接游标
cur.execute("SELECT * from kqecshop_user u where u.telephone IN('15828022852','18180734223') and u.compIdentification=10000; ")
#注意这里的语句后面有分号
#fetchall取所有行
for r in cur.fetchall():
           print(r)
           print (type(r))
           print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
           #cur.close()
conn.close()