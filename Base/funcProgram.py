#!/usr/bin/env python
# -*- coding:utf-8 -*-

#函数式编程，主要是把函数作为参数，返回值也是函数

# 高阶函数 : 把函数A作为参数传给函数B，那么函数B就被称为高阶函数
# 函数名也是变量

#举例，一个简单的高阶函数
def add(x,y,f):
	return f(x) + f(y)

print add(-5,-8,abs)


# map/reduce
# 1 map函数：map函数接收两个参数，一个是函数，一个是序列， map将传入的函数一次作用到序列的每个元素，并把结果作为新的list返回

#例如 ： 函数为f(x) = 1 + x*x , 序列为 [1,2,3,4,5,6]
def f(x):
	return 1 + x*x
print map(f,[1,2,3,4,5,6])

# 由此可见，map也是一个高阶函数
print map(str,[1,2,3,4,5,6]) #list的元素转为字符串


# 2 reduce 把结果继续和序列的下一个元素做累积，而reduce接受的函数，必须传两个参数	，其效果就是：reduce(f, [x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
# 如对一个序列求和

def add(x,y): #注意这个函数必须是两个参数
	return x + y
print reduce(add, range(1,101))

#例如，将 1，3，5，7，9变为13579
def fn(x,y):
	return 10*x + y
print reduce(fn,[1,3,5,7,9])


#配合map,我们就可以写出把str 转换为int的函数

def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

print reduce(fn,map(char2num, '13579')) #解析： map之后得到一个新的list【1，3，5，7，9】,再把这个list ，与fn进行组合，reduce，得到一个新的整数13579

#整理成一个str2int(s):
def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2num(s):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	return reduce(fn, map(char2num,s))

#还可以用lambda函数进一步简化成：
def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
def str2int(s):
	return reduce(lambda x,y: x*10+y, map(char2num,s)) #lambda,后期再说使用方法


#练习：
def CapStr(name):
	return name.capitalize()

print map(CapStr,['aa','bb','cc'])

#filter，也是高阶函数，接受一个函数，一个list,函数作业与list的每一个元素，然后根据返回值为true or false，选择保留还是丢弃

def is_odd(n):
	return n%2 == 1

print filter(is_odd, [1,2,3,4,5])

# 把一个空字符串删掉
def not_empty(s):
	return s and s.strip()

print filter(not_empty,["ad", None, "", "dd", "   "])

# 尝试用 filter 删除1-100的素数
def issuShu(n):
	for a in range(2,n):
		if n%a==0:
			return False 
		elif a == n - 1:
			return True

print filter(issuShu,range(1,101))

#排序算法 sort
	
print sorted([36, 5, 12, 9, 21])

# sorted 也是一个高阶函数，也可以进行自定义，倒序，升序
def reversed_cmp(x, y):
	if x>y:
		return -1
	elif x<y:
		return 1
	else:
		return 0

print sorted([36, 5, 12, 9, 21],reversed_cmp)


#字符串的排序
print sorted(['bob', 'about', 'Zoo', 'Credit'])#默认情况下，对字符串排序，是按照ASCII的大小比较的,即区分大小写


def cmp_ignore_case(s1,s2):
	u1 = s1.upper() # 先变为大写
	u2 = s2.upper()
	if u1 < u2:
		return -1
	elif u1 > u2:
		return 1
	else: 
		return 0
print sorted(['bob', 'about', 'Zoo','Credit'], cmp_ignore_case)


# 返回函数
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

#如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办?可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum 

#当我们调用 lazy_sum() 时，返回的并不是求和结果，而是求和函数:

f = lazy_sum(1,3,5,7,9)
print f() #当 lazy_sum 返回函数 sum 时，相关参数和变量都保存在返回的函数中，这种称为“闭包(Closur e)”的程序结构拥有极大的威力。

def count():
	fs = []
	for i in range (1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1, f2, f3 = count()

print f1(),f2(),f3() #全部都是 9 !原因就在于返回的函数引用了变量 i ，但它并非立刻执行。等到3个函数都返回时，它们所引用的变 量 i 已经变成了3，因此最终结果为 9 

#  返回闭包时牢记的一点就是:返回函数不要引用任何循环变量，或者后续会发生变化的变量。


#如果一定要引用循环变量怎么办?方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变 量后续如何更改，已绑定到函数参数的值不变:

def count():
	gs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j*j
			return g
		gs.append(f(i)) # 此处保存的是g函数
	return gs

g1, g2, g3 = count()
print g1(),g2(),g3()


a,b,c = [1,2,3]
print a, b, c

#匿名函数

# 当我们在传入函数时： 有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
# 匿名函数的关键字用lambda

'''
关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数。 匿名函数有个限制，就是只能有一个表达式，不用写 return ，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿
名函数赋值给一个变量，再利用变量来调用该函数:
'''
# 如：
print map(lambda x: x*x, [1,2,3,4,5,6,7])

#匿名函数 lambda x: x * x 实际上就是:

def f(x):
	return x*x

# 装饰器：
def now():
	print '2017-8-6'
f = now
f() 
# 函数对象也有一个 __name__属性，可以拿到函数的名字：
print now. __name__ 	

# 假设我们要增强 now() 函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改 now() 函数的定 义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator)。

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下:


def log (func):
	def wrapper(*args,**kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper

@log  #把 @log 放到 now() 函数的定义处，相当于执行了语句: now1 = log(now1)
def now1():
	print '2017-8-6'
now1()

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义 log的文本:

def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print 'call %s %s():' % (text,func.__name__)
			return func(*args, **kw) 
		return wrapper
	return decorator

@log('execute')   #now = log('execute')(now)
def now2():
	print '2013-12-25'

now2()

print now2.__name__

#剖析上面的语句，首先执行 log('execute') ，返回的是 decorator 函数，再调用返回的函数，参数是 now 函 数，返回值最终是 wrapper 函数。


#注意：
'''
以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有 __name__ 等属性，但 你去看经过decorator装饰之后的函数，它们的 __name__ 已经从原来的 'now' 变成了 'wrapper' :
 now.__name__
  'wrapper'
因为返回的那个 wrapper() 函数名字就是 'wrapper' ，所以，需要把原始函数的 __name__ 等属性复制 到 wrapper() 函数中，否则，有些依赖函数签名的代码执行就会出错。
不需要编写 wrapper.__name__ = func.__name__ 这样的代码，Python内置的 functools.wraps 就是干这个事的，所 以，一个完整的decorator的写法如下:
'''

import functools
def log2 (func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call %s():' %func.__name__
		return func(*args,**kw)
	return wrapper


@log2
def now3():
	print "2017-8-8"

now3()	

print now3.__name__


''''
练习
'''

def exercise(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print "begin call"
		func_temp = func(*args,**kw)
		print "end call"
		return func_temp
	return wrapper

@exercise
def now4():
	print "2017-8-8"

now4()	


#偏函数：
#Python的 functools 模块 供了很多有用的功能，其中一个就是偏函数(Partial function)。要注意，这里的偏函 数和数学意义上的偏函数不一样。

#例如
import functools
int2 = functools.partial(int, base = 2) #int("12",base=10),默认转为10进制

print int2('100000')

# 注意到上面的新的 int2 函数，仅仅是把 base 参数重新设定默认值为 2 ，但也可以在函数调用时传入其他值:
print int2("100000",base = 10)

# 创建偏函数时，实际上可以接收函数对象，*args和**kw这3参数
#上面的例子实际上是固定了base参数，相当于：
kw = {"base": 2}
print int('1000',**kw)

#当函数的参数个数太多，需要简化时，使用 functools.partial 可以创建一个新的函数，这个新函数可以固定住原函 数的部分参数，从而在调用时更简单。

