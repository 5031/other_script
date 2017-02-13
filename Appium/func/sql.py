#!/usr/bin/env python
#_*_ coding=utf-8 _*_
#Date:2016-12-28 PASS
_author_ = 'wenzhe'

import pymysql
import configparser
import os

def read_conf():
    base_dir = os.path.dirname(os.path.dirname(__file__))  # os.path.dirname  返回一个目录名组件 __file__:代表py文件路径
    base_dir = str(base_dir)  # 转换为字符串后，才有split方法
    spell = base_dir + '/models/service.conf'
    print(spell)
    conf = configparser.ConfigParser()
    conf.read(spell)
    return conf

def query_pay(pay_num):
    conn= pymysql.connect(host='192.168.0.105', port=3306, user='root', passwd='hyt@root@123',db='hyt_ecshop',charset='utf8')
    cur = conn.cursor()
    cur.execute("select o.payOrderNum,o.total_price from kqecshop_ordermain o WHERE o.num = %s ;" % pay_num )
    result = cur.fetchall()
    pay_num = result[0][0]
    pay_mon = int(result[0][1] * 100)       #转化为int
    #print (pay_num,pay_mon)
    return (result[0][0],result[0][1])      #返回订单，支付金额

def pingou_set(fight_purchase_title):
    '''除‘自动化测试_别改’外，其它都设置为不置顶,置顶时间为NULL   PASS'''
    conn = pymysql.connect(host='192.168.0.105', port=3306, user='root', passwd='hyt@root@123', db='hyt_market',charset='utf8')
    cur = conn.cursor()
    cur.execute("UPDATE fight_purchase  SET has_top = 0,top_date = NULL  where fight_purchase_title != %d;" % (fight_purchase_title))
    conn.commit()
    result = cur.fetchall()
    return (result)  # 返回订单，支付金额


if __name__ =='__main__':
    list = query_pay(17347)
    print (list)
    pingou_set(10049)
    read_conf()
