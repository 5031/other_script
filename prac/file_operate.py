# -*- coding:utf-8 -*-
#找到文件 E:\log

#打开文件
file_obj = open('D:\Job\python\code\other_script\prac\\file_operate.txt','a')

#错误的类型定义会导致能使用的方法不同
my_list = []
#读取去全部内部文件
#print file_txt2.read()
#单行读取
#print file_txt2.readinto()
#以单行读取的方式读取多行
line_list = file_obj.readlines()
print (line_list)
#分行读取出来
for i in line_list:
    # 去掉结果中的换行符
    ele = i.strip()
    ele_value = ele.split(":")
    #print "ele_value:%s" % ele_value
    #强制转换为int类型
    ele_value_last = int(ele_value[-1])
    #print  "ele_value_last:%s" % ele_value_last
    ele_value_last +=  1
    #将更新后的值替换到list中最后一个值
    ele_value[-1] = str(ele_value_last)
    #这里的输出并未影响岛原文件，
    print ("update ele_value is:%s" % ele_value)
    #将list合并为字符串
    recover_value = ":".join(ele_value)
    #设置接收局部变量的全局变量
    my_list.append(recover_value)
    print (my_list)
#recover_value各个元素通过\n拼接起来---这里有问题
my_str = "\n".join(my_list)
print (my_str)
file_obj.write(my_str)
file_obj.close()

