#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
#Date:2017-02-05 Pass

from appium import webdriver
import pymysql,json,requests
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# from .pay import pay
# from .sql import query_pay

def pay(pay_num,pay_mon,pay_way):
    '''支付接口回调'''
    headers = {
        'Connection': 'keep - alive',
        'Version': '1.8.5',
        'From':'2',
        'Bind-ID': '10000',
        'interfaceVersion': '1.0',
        'Content - Type': 'application / x - www - form - urlencoded',
        'Host':'192.168.0.104:8081',
        'User - Agent':'Apache - HttpClient / 4.5.2(Java / 1.8.0_45)'}
    jsonstr = json.dumps({"retry_counter": '0', "retryCounter": '0', "transaction_id": pay_num, "transactionId": pay_num,"transaction_fee": pay_mon, "transactionFee": pay_mon, "channel_type": pay_way, "channelType": pay_way, "transaction_type": "PAY", "transactionType": "PAY",
                           "notify_url": "http://hyttest.hyuntao.com:8089/beecloud_pay_notify.htm","notifyUrl": "http://hyttest.hyuntao.com:8089/beecloud_pay_notify.htm", "tradeSuccess": 'true',"trade_success": 'true', "sub_channel_type": "UN_APP", "optional": {},"id": "ec2b7cfb-fcfd-40d0-ba73-2ecba0887109",
                           "messageDetail": {"bizType": "000201", "orderId": pay_num, "txnSubType": "01",
                                             "signature": "Jgkktl8Lun0/wg75XwH22UnS4OtWbiFnAnrhkAXDpSZdPbTjROawFBIXdXXAAy2zEFCaaTMFX8vMr/G5RXRtLEk8NzSupNjuiB2wwLJMNzTf2j0oIy7dE8v3195RIPzA5OLUYkfZmlT   QsyZVAD9QrYlNUpOsdA6HVPkmoZT1qPcJqSV7tYADchdF/o99R6EAbHlce8Qb8zr47dYnNBMV/oqSlyZP1xD7732vKAuj49/0RetC3sZ0bYpRmiPRWmu2MtfSj4Ywcw0hJpxKerz3pE3f/TOaOy9W11EH/x2QKIvCK5Ia/bLPpfHIKiIlpkzIgtxVFaTl8o26XKQbXA==",
                                             "traceNo": "309399", "settleAmt": "1", "settleCurrencyCode": "156", "settleDate": "0303", "txnType": "01", "certId": "69597475696",
                                             "encoding": "UTF-8", "version": "5.0.0", "queryId": "201603031617533093998","trade_no": "2016102521001004780295435599",
                                             "transaction_id": "4001852001201610257645654581", "accessType": "0","tradeSuccess": 'true', "respMsg": "Success!", "traceTime": "0303161753",
                                             "txnTime": "20160303161753", "merId": "308510148991005", "currencyCode": "156","respCode": "00", "signMethod": "01", "txnAmt": "1"},
                           "message_detail": {"bizType": "000201", "orderId": pay_num, "txnSubType": "01",
                                              "signature": "Jgkktl8Lun0/wg75XwH22UnS4OtWbiFnAnrhkAXDpSZdPbTjROawFBIXdXXAAy2zEFCaaTMFX8vMr/G5RXRtLEk8NzSupNjuiB2wwLJMNzTf2j0oIy7dE8v3195RIPzA5OLUYkfZmlT   QsyZVAD9QrYlNUpOsdA6HVPkmoZT1qPcJqSV7tYADchdF/o99R6EAbHlce8Qb8zr47dYnNBMV/oqSlyZP1xD7732vKAuj49/0RetC3sZ0bYpRmiPRWmu2MtfSj4Ywcw0hJpxKerz3pE3f/TOaOy9W11EH/x2QKIvCK5Ia/bLPpfHIKiIlpkzIgtxVFaTl8o26XKQbXA==",
                                              "traceNo": "309399", "settleAmt": "1", "settleCurrencyCode": "156", "settleDate": "0303", "txnType": "01", "certId": "69597475696","encoding": "UTF-8", "version": "5.0.0", "queryId": "201603031617533093998","trade_no": "2016102521001004780295435599",
                                              "transaction_id": "4001852001201610257645654581", "accessType": "0","tradeSuccess": 'true', "respMsg": "Success!", "traceTime": "0303161753","txnTime": "20160303161753", "merId": "308510148991005","currencyCode": "156", "respCode": "00", "signMethod": "01", "txnAmt": "1"},"sign": "446e9d5ea190b6c030b6a912c8fba05c", "signAll": "e2aa12b84581acd8ac78e818cec713c3","timestamp": '1456993860000'})
    pay = {'requestType': '1', 'signature': 'f8a5d31632c6844d1cd922bf1d0b89ca','requestJson':jsonstr}
    #print ('pay:',pay)
    r = requests.post('http://192.168.0.104:8081/app/beecloud_pay_notify.htm',data=pay,headers=headers)
    #print (r.url)
    print (r.status_code)
    print (r.text)

def query_pay(pay_num):
    conn= pymysql.connect(host='192.168.0.105', port=3306, user='root', passwd='hyt@root@123',db='hyt_ecshop')
    cur = conn.cursor()
    cur.execute("select o.payOrderNum,o.total_price from kqecshop_ordermain o WHERE o.num = %s ;" % pay_num )
    result = cur.fetchall()
    pay_num = result[0][0]
    pay_mon = int(result[0][1] * 100)       #转化为int
    #print (pay_num,pay_mon)
    return (result[0][0],result[0][1])      #返回订单，支付金额

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'note2'
#apk包名
desired_caps['appPackage'] = 'com.android.kangqi.youping'
#apk的launcherActivity
desired_caps['appActivity'] = 'com.android.kangqi.youping.activity.ActStart'

#启动
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

# driver.wait_activity('.activity.ActHome',60,1)
print ('首页:',driver.current_activity)
sleep(10)
# driver.find_element_by_name(u'品牌').click()      #通过name和selenium用法相同
# driver.find_element_by_id('btn_brand').click()    #通过id定位--品牌
#driver.find_element_by_name(u'输入商品名称搜索').click()    #对应layout中的id后半截--进入随览
driver.find_element_by_id('iv_search').click()          #点击搜索图标
print (u'搜索:',driver.current_activity)
driver.find_element_by_id('ed_search').click()              #搜索框输入信息
driver.find_element_by_id('ed_search').send_keys(u'testfee')     #
driver.find_element_by_id('tv_search').click()              #点击搜索

driver.find_element_by_id('image_bar').click()              #点击商品主图
sleep(2)
driver.find_element_by_id('goods_buyNow').click()           #点击立即购买
# sleep(1)
# driver.find_element_by_id('acc_phone').send_keys(u'15008499834')        #输入用户名
# driver.find_element_by_id('acc_password').send_keys(u'123456')
# driver.find_element_by_id('button_login').click()                       #登录
# sleep(1)
# driver.find_element_by_id('goods_buyNow').click()           #再次点击立即购买
# print (u'商品详情:',driver.current_activity)
sleep(2)
driver.find_element_by_id('goods_buyNumber').send_keys('2')  #修改数量
driver.find_element_by_id('btn_ok').click()                     #点击‘确定’,进入结算中心
print (u'结算中心:',driver.current_activity)
sleep(10)
driver.find_element_by_id('submit_button').click()
print (u'结算中心:',driver.current_activity)
sleep(10)
driver.find_element_by_id('pay_submit').click()                 #选择支付方式
sleep(19)
driver.back()
#会回到支付失败
sleep(10)
driver.find_element_by_id('tv_back').click()                    #点击返回
driver.find_element_by_id('confirm_button').click()             #点击‘确定’
sleep(5)
driver.find_element_by_name(u'待付款').click()                 #进入待付款
sleep(3)
#找到第一个订单信息，点击
driver.find_elements_by_id('order_goods')[0].click()           #点击订单商品

x = driver.get_window_size()['width']
y = driver.get_window_size()['height']

x1 = int(x * 0.5)
y1 = int(y * 0.75)
y2 = int(y * 0.70)

driver.swipe(x1,y1,x1,y2,1000)                             #不得行
# ActionChains(driver).move_to_element(driver.find_element_by_id('tv_shouldPay')).perform()        #移动屏幕---需要依赖元素显示在屏幕中；移动到相邻元素--不可移动屏幕
order_num =  driver.find_element_by_id('order_no').text      #获取详情总点单编号模块内容，通过pay支付
list = query_pay(order_num)
pay(list[0], float(list[1]) * 100, 'UN')                    #z支付

driver.refresh()
driver.quit()







