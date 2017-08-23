#!/usr/bin/env python
# -*- coding:utf-8 -*-

#函数中的可变参数
#定义可变参数，在参数前面加一个* ，此时可以传入list 或者tupe
def cale (*number):
	sum = 0
	for n in number:
		sum += n*n
	return sum
print cale(1,2) #传入的是一个元祖，省略了（）

# 2. 如果已经有一个list 或者tupe 需要作为参数传进去，则按照如下调用，且是非常常见 ,当然也可以还原为tupe形式
list1 = [1,2,3]
print cale(*list1)

# 3. 关键字参数： 自动组装0个或任意个参数名的参数，关键字参数在函数内部，自动组装为字典
def person(name, age, **kw):
	print "name:", name, "age:", age, "other", kw
#解析上面方法： name, age, 为必选参数，kw为关键字参数(可任意多个字段)，带**
person("xiaoming",18)
person("xiaoming",18,city = "guangzhou", sex = "man", work = "doctor")

# 当然 也可以直接传一个字典，但要在前面加**
dic1 = {"city" : "guangzhou", "sex": "man", "work": "doctor", "father": "army"}
person("xiaowang", 27, **dic1)

#参数组合：在函数参数中 可以同时使用 必选参数，默认参数，可变参数，关键字参数，但是在定义时，必须按照：必选参数，默认参数，可变参数，关键字参数 这个顺序来定义。

def func(a, b, c = 0, *args, **kw):
	print "a=", a, "b=", b, "c=", c, "args=", args, "kw=", kw

func(1,2)
func(1,2,3)
func(1,2,3,"a","b")
func(1,2,3,"a","b",cc="x")

#最神奇的是你可以通过一个 tupe 和dict 调用这儿func
list2 = (1,2,3,4,5)
dict2 = {"x": "a", "y": "b"} 
func(*list2, **dict2)


#* 第二章：递归
def fac(n):
	if n == 1:
		return 1
	return n * fac(n-1)
print fac(10)

# 尾随递归

def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1,num * product)

print fact(5)















