#!/usr/bin/env python
# -*- coding:utf-8 -*-
_author_ = 'wenzhe'

# name = input('input your name').strip()       #还是需要加strip(),不会主动取出空格
# print (name)

import subprocess,time                           #使用python自带的subprocess库；此模块允许您生成进程，连接到输入/输出/错误管道，并获得它们的返回代码。
# exename = 'C:\\Users\SH\Desktop\hub.bat'                    #指定外部exe程序的路径。并指定传入参数，注意使用二进制格式传入
# p = subprocess.Popen(exename,stdin=subprocess.PIPE,stdout=subprocess.PIPE)      #subprocess的Popen方法有很多的参数，对于初学者而言，不必深究。这里我以 后缀表达式的转换程序为例。传入参数为字符串，传出也是字符串。两个进程建立pipe管道通信。请仔细体会参数的使用。p.communicate()方法返回的是元组，可根据自己需求选取元素。该方法同时传入参数，input=，就是传参。
# result = p.communicate()
# res = result[0]                                 ##程序运行，显示出exe程序执行的结果。相关结果已经处理，去掉不需要的部分，并且转换成字符串格式
# print (res)

#这个启动貌似只能运行一个实例
exelist = []
exelist.insert(0,'C:\\Users\SH\Desktop\hub.bat')
#exelist.append('C:\\Users\SH\Desktop\\node.bat')       #会导致重复添加
exelist.insert(1,'C:\\Users\SH\Desktop\\node.bat')
for i in range(len(exelist)):
    p = subprocess.Popen(exelist[i], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    result = p.communicate()

