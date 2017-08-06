#!/usr/bin/env python
# -*- coding:utf-8 -*-

#生成器，一边循环，一边计算的机制，称为生成器，没用到的变量暂不创建，主要用来节约空间内存

#创建方法：把列表生成式（） 改为【】
g = (x*x for x in range(10))
print g

# 生成器，每次调用 next()，就计算出下一个元素的值，直至最后一个值，没有更多元素时，则会抛出stopLteration的错误

# 生成器的另外一种调用可以用for循环进行迭代 generator 也是可迭代的
for n in g:
	print n

#计算著名的费拉切数列
def fib(max):
	n = 0
	a = 0
	b = 1
	
	while n < max:
		print b
		a = b
		b = a + b
		n = n + 1

fib(20)
#生成器的另一种定义方式：
# 如果 一个函数定义中包含yield 关键字，那么这个函数就不再是一个普通函数，而是一个genertaor

# 注意： genertaor 函数，同普通的函数调用不一样，每次调用next()的时候执行，遇到yield 语句返回，再次执行时，从上次返回的yield语句处继续执行

# 1 1 2 3 5 8 13 21 
def fib2(max):
	n = 0
	a = 0
	b = 1
	while n < max:
		yield b
		a = b
		b = a + b
		n=n+1

g2 = fib2(5)
print g2
print g2.next()

for n in g2:
	print n



