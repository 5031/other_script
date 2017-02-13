#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

import time,datetime
now = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())        #时间格式输出
print (now)

n= time.gmtime()
print (type(n))

def datetime_add1():        #实现时间加一天
    now = datetime.datetime.now()
    date = now + datetime.timedelta(days=1)
    date = str(date).split('.')[0]
    return date