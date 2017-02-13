#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

from os import system,popen
from os import *        #不建议使用
system('ipconfig')        #打印命令结果
print ('>>>>>>>>>>')
res = popen('ipconfig').read()  #打印命令结果
print (res)
