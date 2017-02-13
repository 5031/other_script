#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)

#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)

#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,u'ue035')