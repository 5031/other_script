#!/usr/bin/env python
#_*_ coding=utf-8 _*_
_author_ = 'wenzhe'

import requests
#payload = {'key1':'hello','key2':'world','key3':None}       #值为None的键不会被添加到URL的查询字符里
# r = requests.get('http://www.baidu.com',params=payload)
# print (r.url)       #查看编码后的url
#
# #4,unicode响应内容
# r = requests.get('https://github.com/timeline.json')
# print (r.text)        #text:Content of the response, in unicode.
# #Requests会自动解码来自服务器的内容。大多数unicode字符集都能被无缝地解码。请求发出后，Requests会基于HTTP头部对响应的编码作出有根据的推测。当你访问r.text之时，Requests会使用其推测的文本编码。你可以找出Requests使用了什么编码，并且能够使用r.encoding 属性来改变它

#5,二进制响应内容
#如果访问返回的内容是二进制的图片，你可以使用r.content访问请求体
# from PIL import Image
# from io import BytesIO
# import requests
# r = requests.get('http://cn.python-requests.org/zh_CN/latest/_static/requests-sidebar.png')
# i = Image.open(BytesIO(r.content))
# i.show()

# #6,JSON响应内容：
#     #Requests中也有一个内置的JSON解码器，助你处理JSON数据：
# import requests
# r = requests.get("https://github.com/timeline.json")
# print (r.json())

# #7,定制请求头
# #   如果你想为请求添加HTTP头部，只要简单地传递一个 dict 给headers 参数就可以了
# import requests
# import json
# payload = {'some':'data'}
# headers = {'content-type':'application/json'}
#r = requests.get('https://github.com/timeline.json',data = json.dumps(payload),headers = headers)
# print (r.json())
# #注意，这里的payload是放到body里面的，所以params参数要使用json数据

#9,POST请求就像上面‘定制请求头’中的例子，将payload序列化为json格式数据，传递给data参数。
# import requests
# url = 'http://httpbin.org/post'
# files = {'file':open('test.txt','rb')}
# r = requests.post(url,files= files)
# print (r.text)

#10,post 提交表单
# 传递一个字典给data参数就可以了。数据字典在发出请求时会自动编码为表单形式
# payload = {'key1':'value1','key2':'value2'}
# r = requests.post('http://httpbin.org/post',data=payload)
# print(r.text)

#11,响应状态吗
#   使用r.status_code返回相应的状态码
# r = requests.get('http://httpbin.org/get')
# print (r.status_code)
# #为方便引用，Requests还附带了一个内置的状态码查询对象：
# print (r.status_code == requests.codes.ok )

#12，失败请求抛出异常
#   如果发送了一个失败请求(非200响应),我们可以通过
# bad_url = requests.get('http://httpbin.org/status/404')
# print (bad_url.status_code)
# bad_url.raise_for_status()
# print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# #如果返回码是200，则不会抛出异常
# bad_url = requests.get('http://httpbin.org/get')
# print (bad_url.status_code)
# bad_url.raise_for_status()

# 13,响应头
#   我们可以查看以python字典形式展示的服务器响应头
# r = requests.get('http://httpbin.org/get')
# print (r.text)
# print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# print (r.headers)
# print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# print (r.headers['Connection'])             #header是字典类型

# 14，cookies
# 得到响应中包含的一些cookies：
# url= 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# print(r.cookies)
#要想发送你的cookies到服务器，可以使用cookies参数
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are = 'working')
# r = requests.get(url,cookies=cookies)
# print (r.text)

#15,重定向与请求历史
#默认情况下，除了head，requests会自动处理所有重定向。
#可以使用响应对象的history方法来追踪重定向
# r = requests.get('http://github.com')
# print ('url:',r.url)
# print ('status_code:',r.status_code)
# print ('history:',r.history)
# #如果你使用的是GET, OPTIONS, POST, PUT, PATCH 或者 DELETE,，那么你可以通过 allow_redirects 参数禁用重定向处理
# r = requests.get('http://github.com', allow_redirects=False)
# print ('status_code:',r.status_code)
# print ('history:',r.history)
# #如果你使用的是HEAD，你也可以启用重定向:
# r = requests.head('http://github.com', allow_redirects=True)
# print ('status_code:',r.status_code)
# print ('history:',r.history)