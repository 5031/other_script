#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

from urllib import request      #引入urllib下的request
print(request.__file__)          #查看py文件路径
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from pytesseract import pytesseract

img_url ='http://mimg.127.net/logo/163logo.gif'
img_jpg = 'D:\Job\python\code\other_script\prac\save_img.jpg'

def saveImg(imageURL, fileName):
    u = request.urlopen(imageURL)
    data = u.read()
    f = open(fileName, 'wb')
    f.write(data)
    f.close()

def pic_ocr(var):
    im = Image.open(var)
    #imgry = im.convert('L')
    num = pytesseract.image_to_string(im)
    return num

if __name__ == '__main__':
    d = webdriver.Chrome()
    d.get('http://192.168.0.104:8085/plat/admin/login.htm')
    pic_url = d.find_element(By.CLASS_NAME,'yzm_icon').get_attribute('src')
    print (pic_url)
    saveImg(pic_url,'save_img.jpg')
    num = pic_ocr('D:\Job\python\code\other_script\prac\save_img.jpg')
    num = num
    print (num)
