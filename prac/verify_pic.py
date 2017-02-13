#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'
#Date:2016-12-29  False

from PIL import Image
from io import BytesIO
import pytesseract
import os
import requests
if '__name_' == '__main__':
    r = requests.get('http://192.168.0.104:8082/verify')
    i = Image.open(BytesIO(r.content))
    i.save(os.path.join('test.jpg'))
    # # i = i.convert('L')
    # #i.show()
    print(pytesseract.image_to_string("test.jpg"))        #识别验证码动作
    print(os.path.dirname(os.path.dirname('__file__')))