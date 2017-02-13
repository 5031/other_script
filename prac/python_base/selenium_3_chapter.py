# #!/usr/bin/env python
# #_*_ coding=utf-8 _*_
# _author_ = 'wenzhe'

#   3.2 输入与输出
#       3.2.1 打印
print('hello %s,Nice to meet you !' % 'Li')
print ('hello %r,Nice to meet you !' % 'Li')        #如果不知道打印类型，就用r%

name = 'i am {0},age {1}'       #python中特有占位符，需通过格式化进行赋值,索引从0开始
name1 = name.format('alex',20)
print (name1)


#       3.2.2 input输入
# name = input("Enter your name:")
# print ('print your name: %r' % name)

#       3.2.3 引号与注释
#           在python中，不区分单引号与双引号；但是二者需要配套使用，不能交叉使用

#   3.3 分支与循环
#       # 3.3.1 if语句
#           if语句来实现分支判断，一般语法是if...elif...else:
#       # 3.3.2 for语句
#           for循环的使用更加灵活/简单
for i in 'hello world':  #这里会打印每个字符
    print (i)
print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
fruit = ['banana','apple','juice']
for i in fruit:             #循环列表
    print (i)
print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
for i in range(1,5,2):          #循环固定次数,开始/结束/步长
    print (i)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
for i in range(len(fruit)):        #当不知道循环次数，用len
    print (i)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

#   3.4 数组和字典
#       3.4.1 数组
list = [1,2,3,'a','b','c']
list.append('z')
list.insert(0,-1)
print (list)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#       3.4.2 字典
dict_name = {
    'name':'alex',
    'age':18,
    'job':'IT Dog'
}
print (dict_name.keys())
print (dict_name.values())
print (dict_name.items())       #将所有字典项以列表方式返回
for k,v in dict_name.items():   #这里获得2个var
    print ('dict key is:',k)
    print('dict value is:', v)
#
keys = ['a','c','e','a']
values = [1,2,3,4]
for keys,values in zip(keys,values):        #zip合并两个list为dict，并且按原先顺序输出
    print (keys,values)
new_dict = zip(keys,values)
print (new_dict)                        #????????????????
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

  # 3.5 函数/类/方法
  #     3.5.1 函数
def add_num(a,b):
    return a + b
#print (add_num(3,'a'))      #int和str不能直接相加
print (add_num(100,12))

def add_num2(a=10,b=20):      #设置默认参数
    return a+b
print (add_num2())
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
      # 3.5.2 类和方法
      #     在面向对象编程的世界里，一切皆为对象，抽象的一组对象就是类。例如汽车就是一个类，章三家的奇瑞汽车就是
      #     一个具体的对象
class A(object):            #object为所有类的基类，python3中已经可以不写出来了

    def __init__(self,a,b): #当我们调用A类的时候，就首先会执行他的init方法，所以需要对齐进行传参
        self.a = int(a)
        self.b = int(b)

    def add(self):      #类中的方法必须包含self，它是指对象本身，在调用这个方法的时候不用为这个参数赋值
        return self.a + self.b

count = A(4,5)
print (count.add())

class B(A):             #继承A中的所有方法和类变量
    def sub(self):
        return self.a - self.b
count = B(5,2)
print (count.sub())

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

#   3.6 模组：库或模块
#       3.6.2 模块调用
#           不使用unitest框架，调用同级目录模块方法：
#               from pub import add
#       3.6.3 跨目录模块调用：不使用unitest框架，调用同级目录下的子文件
#                from model.pub import add    model--同级目录
#                 import转载的顺序是查找当前路径以及当前指定的sys.path，然后再是python安装时设置的相关默认路径。如果当前路径
# 或指定路径存在与当前标准mod同样的moduleule，则会覆盖标准module，那么导入的就是当前目录下的。
#                 解决办法是 from .count import A 价格点，是用来告诉调用程序count是相对于new_count.py的一个引入
#                 如果这样修改提示:未加载父母快，不能执行导入，就在代码中增加 sys.path.append('./model')  将model目录添加到系统环境变量path中
#
#   3.7 异常
#       如果知道异常，那么我们就可以通过python提供的try...except..语句来接受并处理这个异常
      # 3.7.1 认识异常
try:
    open('abc.txt','r')
except FileNotFoundError as e:       #抛出的错误必须和执行错误一致，否则也会抛出看不懂的信息
    print (e)
#       异常排除机制：1，如果在运行时发生异常，则解释器会查找响应的处理语句(成为handle)。2，如果当前函数里没有找到，则会将异常传递给上层的函数，看看哪里能处理否；3，如果都没有，解释器就会退出，同时打印出tracebac（追溯）
#       Exception是所有异常类的父类；python2.5之后，所有异常类有了新的基类BaseException，二者一样
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
try:
    print (abc)
except BaseException:       #抛出的错误必须和执行错误一致，否则也会抛出看不懂的信息
    print ('文件未发现，主动抛出异常，省略其它看不懂的报错信息')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

try:
    print ('c.txt','r')             #怎么没打印文件没找到呢
    print (abc)
except BaseException as msg:       #msg用于接受异常信息，随后打印
    print (msg)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

#       3.7.2 更多异常
try:
    aa ='异常测试'
    print (aa)
except BaseException as msg:
    print (msg)
else:
    print ('当没有异常就执行这个语句')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

try:
    aa ='异常测试'
    print (d)
except BaseException as msg:
    print (msg)
finally:
    print ('不管是否出现异常，都执行这个语句')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

#       3.7.3 抛出异常
#           pirnt方法只能打印，raise方法可以主动抛出一个异常信息
from random import randint
number = randint(1,10)  #生成一个1到9的随机数
if number % 2 == 0:
    print ('余数为0')
else:
    raise ValueError('This num not div 2，it is: %s ' % number)      #raise只能使用python中所提供的异常类
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')