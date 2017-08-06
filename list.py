#!/usr/bin/env python
# -*- coding:utf-8 -*-

#取list前一部分的值 ------- 切片 （list,tupe，字符串的切片操作是一样的）
list1 = [1,2,3,4,5,6,7]

def getElement(n,*args):
	l = []
	for i in range(n):
		l.append(args[i])
	return l

print getElement(3,*list1)

#一行代码搞定，从0开始，但不包括4，如果第一个元素是0 还可以省略
print list1[0:4]

print list1[:5]

print list1[1:3]

# -1 表示最后一个元素
print list1[-5:]


list2 = range(30) #0 - 29的列表
print list2

#前10个，每两个取一个
print list2[:10:2]


#所有数，每5个取一个
print list2[::5]


# 字符串切
print "zuocaisong"[:7]


# 2 迭代----用for循环来遍历list或者tupe,dic

# 字典默认情况下迭代的是key
dic = {"a":1,"b":2, "c":3}
for key in dic:
	print key

# 迭代出values
for value in dic.values():
	print value


# 迭代出 key: value
# 迭代出values
for key,value in dic.items():
	print key,value  #返回值为tupe,可以省略（）

# 2.2 跌代字符串
for ch in "lyy":
	print ch


#3 判断一个对象是否是可迭代的 用collections模块的iterable
from collections import Iterable
print isinstance("abc",Iterable) #字符串可迭代则返回true


#4,迭代时想获取索引,enumerate
# for i, value in enumerate(['10','11','12'])：
# 	print i, value
#5 ,同时引用两个变量
for x, y in [(1,1),(2,2),(3,3)]:
	print x, y

#4 快速生成一个列表的方式
list3 = [x*x for x in range(1,11)]
print list3 

#还可以加一些条件
list4 = [x*x for x in range(1,11) if x%2 == 0]
print list4

#取列表的值循环时，可以同时取多个变量
dic1 = {'x':'y','Z':'a','B':'c'}
list6 = [k + '=' + v for k, v in dic1.items()]
print list6

list7 = [ch.lower() for ch in list6] # 变为小写
print list7

# 判断一个变量的类型
#如是不是字符串
print isinstance('abc', str)
print isinstance(123,str)

