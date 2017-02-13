#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
# DATE:2016-11-30
# Status：FALSE
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Page(object):         #python3的object是所有类的基类，所有类在创建时默认继承它，所以不用申明继承object也可以
    '''
    页面基础类，用于所有页面的继承
    '''

    def __init__(self,selenium_driver,parent=None):
        self.driver = selenium_driver
        self.parent = parent

    def find_ele_w(self,*func):
        return WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(func))

    def find_ele(self, *loc):
        return self.driver.find_element(*loc)

    def find_eles(self,*loc):
       return self.driver.find_elements(*loc)


    def on_page(self):                          #判定地址
        return self.driver.current_url == (self.base_url + self.url)

    def equal(self,a,b):
        return a == b

    def script(self,src):                       #执行js脚本
        return self.driver.execute_script(src)