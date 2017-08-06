#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

'a test module'
__author__ = 'MIchael Liao'

import sys
def test():
	'''
	 argv 至少有一个元素，因为第一个参数永远是该.py
     文件的名称，例如:
     运行 python hello.py 获得的 sys.argv 就是 ['hello.py'] ;
	'''

	args = sys.argv # argv 变量，用list存储了命令行的所有参数
	if len(args) == 1:
		print "hello world!"
	elif len(args) == 2:
		print 'Hello, %s!' % args[1]
	else:
		print 'Too many arguments!'


'''
当我们在命令行运行 hello 模块文件时，Python解释器把一个特殊变量 __name__ 置为 __main__ ，
而如果在其他地 方导入该 hello 模块时， if 判断将失败，因此，这种 if 测试可以让一个模块通过命令行运行时执行一些额外的代 码
'''
if __name__=='__main__': 
	test()

'''
别名
导入模块时，还可以使用别名，这样，可以在运行时根据当前环境选择最合适的模块。
比如Python标准库一般会  供 StringIO 和 cStringIO 两个库，这两个库的接口和功能是一样的，但是 cStringIO 是C写的，速度更快，所 以，你会经常看到这样的写法:
可以优先导入 cStringIO 。如果有些平台不 供 cStringIO ，还可以降级使用 StringIO 。
导入 cStringIO 时，用 import ... as ... 指定了别名 StringIO ，因此，后续代码引用 StringIO 即可正常工作
'''	
try:
	import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
	import StringIO


#z作用域

'''
 1:正常的函数和变量名是公开的(public) ,可以被直接引用，比如: abc ， x123 ， PI 等;
 2: __xxx__ 
 3:类似 _xxx 和 __xxx 这样的函数或变量就是非公开的(private)，不应该被直接引用，比如 _abc ， __abc 等;
 4: 有些时候，你会看到以一个下划线开头的实例变量名，比如 _name ，这样的实例变量外部是可以访问的，
    但是，按 照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随 意访问”。
    之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可
以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量
'''

'''
def _prvi1:
	print "p1"

def _prvi2:
	print "p2"

def pub:
	_prvi1()
	_prvi2()
'''

'''
模块里公开 pub() 函数，而把内部逻辑用private函数隐藏起来了，这样，调用 pub() 函数不用关 心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即:
外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
'''

#关于 在2.7中使用3.0的语法
#如 地板除  在2.7中只会显示整数2 ，在3.0中会显示2.5 如果2.7要显示小数 导入 from __future__ import division (这个在引用时，必须放在代码最上面)
# 如果是3.0想实现 2.7这样的地板流 用 //
print 10/4

print 10//4



'''
小结
由于Python是由社区推动的开源并且免费的开发语言，不受商业公司控制，
因此，Python的改进往往比较激进，不 兼容的情况时有发生。Python为了确保你能顺利过渡到新版本，特别 供了 __future__ 模块，让你在旧的版本中试 验新版本的一些特性。

'''