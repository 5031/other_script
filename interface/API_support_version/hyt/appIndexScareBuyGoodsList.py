#!/usr/bin/env python
#_*_ coding=utf-8 _*_
#Date:2016-12-09
#Status:PASS
_author_ = 'wenzhe'
import requests


def appIndexScareBuyGoodsList(url):
    '''获取app首页最近抢购的三个商品'''
    headers = {
        'Connection': 'keep - alive',
        'Version': '1.8.5',
        'From': '2',
        'Bind-ID': '10000',
        'interfaceVersion': '1.0',
        'Content - Type': 'application / x - www - form - urlencoded',
        'Host': '192.168.0.104:8081',
        'User - Agent': 'Apache - HttpClient / 4.5.2(Java / 1.8.0_45)'
    }
    pay={'signature':'f8a5d31632c6844d1cd922bf1d0b89ca'}
    req = requests.post(url,headers=headers,params=pay)
    #设置编码
    print (req.text)
    print (req.status_code)
    print (req.headers)
    print (req.url)

if __name__ == '__main__':
    url = 'http://192.168.0.104:8081/app/appIndexScareBuyGoodsList.htm'
    appIndexScareBuyGoodsList(url)

