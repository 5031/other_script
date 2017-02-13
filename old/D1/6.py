#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

# name = 'zha'        #name中存入'zha'的内存地址，有索引关系
# name = 'zhong yi'   #重新赋值
# name2 = name        #将name的内存地址copy给name2
# print (name2,id(name2))
# name = 'three'
# print (name2,id(name2))
# del name,name2
#
# ###############--D7---#################
#
# age = 2
# print (type(age))
# age = 2 **16   #还是标准整形
# print (type(age))
# age = 2 ** 32  #长整形了
# print ( type(age))
#
# data = 9.99
# print ('data:',type(data))          #浮点型
# success = False
# print ('bool:',success)             #bool型
#
# ###转换：
# data = 9.99
# data = int(data)                #foat和int可以互相转换
# print ('data:',type(data),' ',data)
#
# name = '10'
# name2= 'abc'
# name = int(name)
# #name = int(name2)               #str部分能和int转换，系统自动判断
#
# success = False
# success = int(success)
# print ('success:',type(success),' ',success)        #bool和int可以互相转换
# success = bool(0)
# print ('success:',type(success),' ',success)

#
# password = 'test'
# for i in range(3):
#     user_input =  input("input password:")
#     if user_input == password:
#         while True:
#             print ("welcome to login:")
#             user_choice = int(input('''
#             1,run a cmd
#             2,exit to level
#             3,logout
#             ''').strip())
#             if user_choice == 1:
#                 print ("run a cmd")
#             elif user_choice == 2:
#                 print ('exit to level')
#                 break               #退出本次循环，进入下次for循环
#             elif user_choice == 3:
#                 print('logout')
#                 exit()              #退出整个代码
#         print ('go to do sth')
#  13  列表
# name_list = ['a','b','c']
# name_list.insert(1,'d')
# print (name_list)
# print (name_list[0:1])      #切片
# print (name_list[-1])       #最后一个
# print (name_list[-2:])      #取出最后2个
# name_list.remove('a')       #移除元素a,如果有多个，就删除第一个
# print (name_list.count('a'))    #统计a出现次数
# for i in range(ame_list.count('a')):    #删除所有元素'a'
#     name_list.remove('a')
#
# #14 字典
# data = {
#     'name':'alex',
#     'age':18
# }
# print (data)        #打印所有数据
# data['nem']= 300    #插入数据
# data['nem']= 400    #修改值
# del data['nem']     #删除
# print (data)
# for k,v in data.items():
#     print (k,v)
# if 'info' in data.keys():       #判断key是否在dict中
#     print (data['info'])
# print (data.get('notvalue'))      #当判断这个元素是否在dict中，用这个比较好，即使没有也会返回None
