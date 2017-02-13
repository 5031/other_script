#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
import time

menu = {
    'sichuan':{
        'chengdu':{
            'chenghua':u'邓超',
            'jinniu':u'吴弈非'
        }
    },
    'hubei':{
        'wuhan':{
            'one':u'文章',
            'tow':u'刘德华'
        }
    }
}
# print (menu['sichuan']['chengdu']['jinniu'][0])       #直接打印最底层值
while True:
    for index,k in enumerate(menu.keys()):     #循环时，直接打印对应索引值
        print ('-->',index,k)
    choice_1 = input('input your choice:')        #python3中，input默认包含了strip方法，所以不用写出来了
    if choice_1.isdigit():                        #用户第一次选择
        choice_1 = int(choice_1)
        ele = list(menu.keys())[choice_1]              #python3中，menu.keys()返回的已经不是list，而是dict_key，所以需要list强制转换
        print (ele)
        # for index,key in enumerate(menu[ele]):
        #     print (index,key)
        for index, k in enumerate(menu[ele].keys()):  # 循环时，直接打印对应索引值
            print('-->-->',index, k)