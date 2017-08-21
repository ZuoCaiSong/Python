#! usr/bin/env python
# -*- coding: utf-8 -*-

import logging 
import pdb

logging.basicConfig(level=logging.INFO)

def foo(s):
	return 10 /int(s)

def bar(s):
	return foo(s)*2

def main():

	try:
		bar('0')
	except StandardError, e:
		logging.exception(e)

main()
#同样是出错，但程序打印完错误信息后会继续执行，并正常退出
print "end"


'''
抛出错误：因为错误是class，捕获一个错误就是捕获到class的一个实例，因此，错误并不是凭空产生的，
Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用 raise 语句抛出一个错误 的实例:
'''
class FooError(StandardError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value :%s' % s)
	return 10 /n

#foo('0')

'''
其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函
数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。

raise 语句如果不带参数，就会把当前错误原样抛出。

 except 中 raise 一个Error，还可以把一种类型的 错误转化成另一种类型:
'''



def foo(s):
	n = int(s)
	return 10/n

def bar(s):
	try:
		return foo(s) * 2
	except StandardError, e:
		print 'error!'
		raise
def main():
	bar('0')

#main()

'''
try:
	10 / 0
except ZeroDivisionError:
	raise ValueError('input error!')

'''

# 断言 assert,为true:则不执行 'n is zero!' ，否则执行 'n is zero!'
# 如果断言失败， assert 语句本身就会抛出 AssertionError :
'''
程序中如果到处充斥着 assert ，和 print 相比也好不到哪去。
不过，启动Python解释器时可以用 -O 参数来关 闭 assert (python -O err.py) :
关闭后，你可以把所有的 assert 语句当成 pass 来看。
'''
def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'

def mian():
	foo('0')

#main()

# 把 print 替换为 logging 是第3种方式，和 assert 比， logging 不会抛出错误，而且可以输出到文件:



s = '0'
n = int(s)

logging.info(' n = %d' % n)
#print 10 / n

'''

这就是 logging 的好处，它允许你指定记录信息的级别，
有 debug ， info ， warning ， error 等几个级别，
当我们 指定 level=INFO 时， logging.debug 就不起作用了。
同理，指定 level=WARNING 后， debug 和 info 就不起作用 了。
这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

'''

'''
pdb
第4种方式是启动Python的调试器pdb，
让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序:

以参数 -m pdb 启动后，pdb定位到下一步要执行的代码 -> s = '0' 。输入命令 l 来查看代码:
输入命令 n 可以单步执行代码:
任何时候都可以输入命令 p 变量名 来查看变量:
输入命令 q 结束调试，退出程序:
'''

'''
这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲 多少命令啊。
还好，我们还有另一种调试方法。
pdb.set_trace() ---- 理解就是设置断点 ，需要导入 import pdb

运行代码，程序会自动在 pdb.set_trace() 暂停并进入pdb调试环境，可以用命令 p 查看变量，或者用命令 c 继续 运行:
'''

print "zcs在下面设置了断点"
pdb.set_trace() # 运行到这里会自动暂停

print "断点解决了"


# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。






