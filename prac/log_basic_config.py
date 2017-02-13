#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

from selenium import webdriver
import logging

logging.basicConfig(level=logging.DEBUG)        #basicConfig()开启的debug模式只能捕捉到客户端向服务器发送的post请求，而无法获取服务器返回的应答请求
d = webdriver.Chrome()
d.get('http://www.baidu.com')
d.find_element_by_id('kw').send_keys('selenium')
d.find_element_by_id('su').click()
d.quit()
