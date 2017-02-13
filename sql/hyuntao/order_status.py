#!/usr/bin/env python
#_*_ coding=utf-8 _*_
#Status：Pass 2017-02-04

_author_ = 'wenzhe'

import pymysql,time

timer = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def update_order_status_20(child_order_num):
    '''修改订单状态为已发货'''
    conn = pymysql.connect(host='192.168.0.105', port=3306, user='root', passwd='hyt@root@123', db='hyt_ecshop',charset='utf8')
    cur = conn.cursor()
    cur.execute("UPDATE kqecshop_orderform  SET order_status = 40 where order_id = %d" % child_order_num)
    conn.commit()
    result = cur.fetchall()
    return (result)  # 返回订单，支付金额

def pingou_set(fight_purchase_title):
    '''除‘自动化测试_别改’外，其它都设置为不置顶,置顶时间为NULL   PASS'''
    conn = pymysql.connect(host='192.168.0.105', port=3306, user='root', passwd='hyt@root@123', db='hyt_market',charset='utf8')
    cur = conn.cursor()
    cur.execute("UPDATE fight_purchase  SET has_top = 0,top_date = NULL  where fight_purchase_title != %d;" % (fight_purchase_title))
    conn.commit()
    result = cur.fetchall()
    return (result)  # 返回订单，支付金额

if __name__ == '__main__':
    # db = pymysql.connect(host='192.168.0.105', port=3306, user='root', passwd='hyt@root@123', db='hyt_ecshop',use_unicode=True, charset="utf8")
    # # 使用cursor()方法获取操作游标
    # cursor = db.cursor()
    # # SQL 插入语句
    # sql = "UPDATE fight_purchase p SET p.has_top=0,p.top_date= NULL where p.fight_purchase_title != 10049;"
    # # db.set_character_set('utf8')
    # cursor.execute('SET NAMES utf8;')
    # cursor.execute('SET CHARACTER SET utf8;')
    # cursor.execute('SET character_set_connection=utf8;')
    # try:
    #     # 执行sql语句
    #     cursor.execute(sql)
    #     # 提交到数据库执行
    #     db.commit()
    #     print(" 没有错误 请党和组织人民放心! ")
    #
    # except Exception as e:
    #     print(e)
    #     # 如果发生错误则回滚
    #     print(" 发生错误")
    #     db.rollback()
    #
    # # 关闭数据库连接
    # db.close()
    pingou_set(10049)

