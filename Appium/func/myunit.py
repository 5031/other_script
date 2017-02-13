#!/usr/bin/env python3
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
# DATE:2016-11-30
# Status：PASS

import unittest,os
from selenium import webdriver

class MyTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'note2'
        # apk包名
        desired_caps['appPackage'] = 'com.android.kangqi.youping'
        # apk的launcherActivity
        desired_caps['appActivity'] = 'com.android.kangqi.youping.activity.ActStart'
        # 启动
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def tearDown(self):
        self.driver.quit()