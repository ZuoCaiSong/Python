#! usr/bin/env pyhton
# -*- coding:utf-8 -*-

'''

动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
 比方说我们要定义一个 Hello 的class，就写一个 hello.py 模块:

'''

class Hello(object):
	def hello(self, name = 'world'):
		print('hello, %s.' % name)

print type(Hello) #Hello 是一个类，他的类型就是type

print(type(Hello())) #h 是一个实例，类型就是class Hello 

'''
我们说class的定义是运行时动态创建的，而创建class的方法就是使用 type() 函数。

要创建一个class对象， type() 函数依次传入3个参数:

1. class的名称;
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法; 
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

通过 type() 函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫 一下class 定义的语法，然后调用 type() 函数创建出class。
'''

def fn(self, name = 'world'):
	print('hello ,%s' % name)

Hello = type('Hello',(object,), dict(hello = fn)) # 创建Hello class

h = Hello()
h.hello()


'''
除了使用 type() 动态创建类以外，要控制类的创建行为，还可以使用metaclass。
'''



'''

当我们认为某些代码可能会出错时，就可以用 try 来运行这段代码，
如果执行出错，则后续代码不会继续执行，而 是直接跳转至错误处理代码，
即 except 语句块，执行完 except 后，如果有 finally 语句块，
则执行 finally 语句 块，至此，执行完毕。

如果没有错误发生，所以 except 语句块不会被执行，
但是 finally 如果有，则一定会被执行(可以没有 finally 语 句)。


'''

try:
	print 'try ...'
	r = 10 / 0
	print 'reuslt:', r
except ZeroDivisionError, e:
	print 'except:', e
finally:
	print 'finally...'
print 'end'	


'''
错误应该有很多种类，如果发生了不同类型的错误，应该由不同的 except 语句块处理。
没错，可以 有多个 except 来捕获不同类型的错误:

此外，如果没有错误发生，可以在 except 语句块后面加一个 else ，当没有错误发生时，会自动执行 else 语句:

Python所有的错误都是从 BaseException 类派生的，常见的错误类型和继承关系看这里:


'''

try: 
	print 'try...'
	r = 10 / int('10')
	print 'result:', r
except ValueError, e:
	print 'ValueError', e
except ZeroDivisionError, e:
	print 'ZeroDivisionError', e

else:
	print 'no error!'
finally:
	print 'finally...'

print 'end'



# 例子
'''
使用 try...except 捕获错误还有一个巨大的好处，就是可以跨越多层调用，
比如函数 main() 调 用 foo() ， 
foo() 调用 bar() ，结果 bar() 出错了，这时，只要 main() 捕获到了，就可以处理:

也就是说，不需要在每个可能出错的地方去捕获错误，
只要在合适的层次去捕获错误就可以了。
这样一来，就大大 减少了写 try...except...finally 的麻烦。
'''
def foo(s):
	return 10/ int(s)

def bar(s):
	return foo(s) * 2

def main():
	bar('0')
	'''
	try:
		bar('0')
	except StandardError, e:
		print e
    finally:
    	print 'finally'
    '''

main()

'''
执行错误信息的第一行

Traceback (most recent call last):
  File "UseTypeCalss.py", line 126, in <module>
    main()
  File "UseTypeCalss.py", line 116, in main
    bar('0')
  File "UseTypeCalss.py", line 113, in bar
    return foo(s) * 2
  File "UseTypeCalss.py", line 110, in foo
    return 10/ int(s)
ZeroDivisionError: integer division or modulo by zero

'''



