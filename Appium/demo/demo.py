#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

import configparser,os

current_dir = os.path.dirname(os.path.dirname(__file__))  # 通过本文件__file__获取相对路径
con = configparser.ConfigParser()
con.read(current_dir + '\data\\test_machine.conf', encoding='utf-8')
u = con.sections()
print (u)