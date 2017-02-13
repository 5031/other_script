#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
#Date:2016-12-24 False

import configparser         #用来读写配置文件


conf = configparser.ConfigParser()
conf.read("D:\\Job\\python\\code\\other_script\\prac\\test.conf",encoding='utf-8')

# 获取指定的section， 指定的option的值
name = conf.get("section1", "name")
print(name)
age = conf.get("section3", "url")
print (age)
