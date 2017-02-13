
#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
#Date:2016-12-30 Pass

from selenium import webdriver
from time import ctime,sleep
from threading import Thread
def test_baidu_multi():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com/")
    driver.find_element_by_id('kw').send_keys('hello')
    driver.find_element_by_id('kw').submit()
    sleep(3)
    driver.quit()

if __name__ == '__main__':
    threads = []
    run_time = 5
    #创建
    for i in range(run_time):
        t = Thread(target=test_baidu_multi,args='')
        threads.append(t)
    #启动
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()
    print ('end: %s' % ctime())
