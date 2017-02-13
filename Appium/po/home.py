#!/usr/bin/env python
#_*_ coding=utf-8 _*_
#PASS 2017-02-06
_author_ = 'wenzhe'
from .base import Page
from selenium.webdriver.common.by import By


class Home(Page):
    search_text = (By.XPATH,'//android.widget.ImageView[@resource-id=\"com.android.kangqi.youping:id/iv_search\"]')  #搜索框
    search=(By.ID,'iv_search')

    def search_text_click(self):
        self.find_ele_w(*self.search_text).click()
