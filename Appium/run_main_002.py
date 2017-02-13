
#_*_ coding=utf-8 _*_
# 2017-01-12 PASS
_author_ = 'wenzhe'

import unittest,time,sys,os
from HTMLTestRunner import HTMLTestRunner
# from bbs.test_case.models.sendmail import sendMail
# from bbs.dir import test_f
#
#指定测试目录
base_url = os.path.dirname(__file__)
base_url = str(base_url)
# print ('test_dir: %s' % tes_dir)
report = base_url + '/report/report'
# print ('report: %s' % report)
discover = unittest.defaultTestLoader.discover(base_url,pattern='test_Level1_0001.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m_%d %H-%M-%S")            #指定时间格式
    filename = report + '/' + now + 'result.html'       #指定报告存放位置，及命名规则
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Android测试',
                            description=u'insist')
    runner.run(discover)
    time.sleep(2)
    fp.close()
    #sendMail()   #频繁发送会被当作垃圾处理




