#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

import sys
sys.path.append("./po")
from time import sleep
from Appium.func.myunit import MyTest
from Appium.po.home import Home

class Android_buy(MyTest):

    def test_0001(self):
        #sleep(15)               #为什么需要sleep
        Home(self.driver).search_text_click()