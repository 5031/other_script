#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

from configparser import ConfigParser
import os

def read_conf():
    base_dir = os.path.dirname(os.path.dirname(__file__))  # os.path.dirname  返回一个目录名组件 __file__:代表py文件路径
    base_dir = str(base_dir)  # 转换为字符串后，才有split方法
    spell = base_dir + '/models/service.conf'
    print(spell)
    conf = ConfigParser()
    conf.read(spell)
    return conf

if __name__ == '__main__':
    test = read_conf()
    print (test)
