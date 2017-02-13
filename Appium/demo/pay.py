#!/usr/bin/env python
#_*_ coding=utf-8 _*_
#STATUS:PASS 2016-12-20
_author_ = 'wenzhe'

import requests
import json
from sql import query_pay
'''
channel_type:"UN"-银联；ALI-阿里；WX--微信
'''

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

if  __name__ == '__main__':
    list = query_pay(17894)
    pay(list[0],float(list[1])*100,'UN')

