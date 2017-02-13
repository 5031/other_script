#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
from selenium.webdriver.common.by import By
from selenium import webdriver

d = webdriver.Chrome()

ele1 = (By.CSS_SELECTOR, 'test')
ele2 = (By.CLASS_NAME, 'test')
ele3 = (By.ID, 'test')

dic = {
    'ele1' : (By.CSS_SELECTOR, 'test'),
    'ele2' : (By.CLASS_NAME, 'test'),
    'ele3' : (By.ID, 'test'),
    'ele4' : (By.LINK_TEXT, 'test'),
    'ele5' : (By.PARTIAL_LINK_TEXT, 'test'),
    'ele6' : (By.NAME, 'test'),
    'ele7' : (By.TAG_NAME, 'test'),
    'ele8' : (By.XPATH, 'test')
}

def choic_by(ele):
    if 'class name' in ele[0]:
        return d.find_element(ele[1])
