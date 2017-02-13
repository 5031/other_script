
#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
#PASS 2017-02-07

# import sys,time
# print (__file__)        #查看当前路径
# print (sys.platform)        #平台信息
# timer = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print (type(timer),timer)

# PASS 02-05:
# f = open('test.conf','r',encoding='utf-8')
# print (f.read())
import time
from selenium import webdriver

d = webdriver.Chrome()
d.get('http://www.hyuntao.com/wxpay104/gym/index?type=1')

time.sleep(10)          #注意时间
d.execute_script("$('[href$=\"256&ptype=1\"]').click();")
time.sleep(8)

#购买手机，弹出提示，也需要js操作
# http://www.hyuntao.com/wxpay104/gym/fitDetail?noNeedSendOut=false&title=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%89%8B%E6%9C%BA1&id=84250&ptype=1
# $('span[type="1"]').click()