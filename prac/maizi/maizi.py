#!/usr/bin/env python
#_*_ coding=utf-8 _*_
#Status：PASS 2017-01-29
_author_ = 'wenzhe'

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.e

url = "http://www.maiziedu.com/"
time = 20
login_txt = u'登录'
account = '15828022852'
pwd = '225410weyd'

#登录
home_login_btn = (By.LINK_TEXT,u'登录')
login_btn =(By.CSS_SELECTOR,'a.a.globalLoginBtn')
account = (By.ID,'id_account_l')

def wait_ele(d,time,func):       #默认值参数放最后
    return WebDriverWait(d,time).until(EC.visibility_of_element_located(func))

def openbrowser():
    return  webdriver.Chrome()

def openurl(url):
    d = openbrowser()
    d.get(url)
    d.maximize_window()

def fine_ele(d,args):
    ''''
    :return must be is tuple
    login_txt
    usernameid
    pwdid
    loginid'''
    if login_txt in args.value():
        ele = WebDriverWait(d,time).until(EC.visibility_of_element_located(home_login_btn))
        ele.click()



def login_test():
    openurl(url)
    ele_dict = {
        'd_home_login_btn':home_login_btn,
        'd_username':account,
        'd_pwd':'pwdid',
        'd_login_brn':login_btn
    }

#判断登录是否正常
try:
    d.find_element_by_css_selector('a.nick')
    print ('Login succes!!')
except:
    print ('Login fails!Check your information!')


d.quit()
--------------------------------------------------------------------------------------------------------------------------------#

