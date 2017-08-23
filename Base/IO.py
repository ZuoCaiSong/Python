#! usr/bin/env pyhton
# -*- coding: utf-8-*-

#1: 打开文件
f = open('/Users/Encore/Desktop/Python3.0/Python/io.txt', 'r')

#2: 如果文件存在调用read方法 
print f.read()

# 3:最后一步是调用 close() 方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操 作系统同一时间能打开的文件数量也是有限的:
f.close()


#如果文件不存在， open() 函数就会抛出一个 IOError 的错误，并且给出错误码和详细的信息告诉你文件不存在:

#f = open('/Users/Encore/Desktop/不存在的文件.rtf', 'r')


'''

由于文件读写时都有可能产生 IOError ，
一旦出错，后面的 f.close() 就不会调用。
所以，为了保证无论是否出错 都能正确地关闭文件，
我们可以使用 try ... finally 来实现:

'''

try:
	f = open('/Users/Encore/Desktop/Python3.0/Python/io.txt', 'r')
	print f.read()
finally:
	if f:
		f.close
'''
但是每次都这么写实在太繁琐，所以，Python引入了 with 语句来自动帮我们调用 close() 方法:
这和前面的 try ... finally 是一样的，但是代码更佳简洁，并且不必调用 f.close() 方法。

调用 read() 会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
所以，要保险起见，可以反复调 用 read(size) 方法，每次最多读取size个字节的内容。
另外，调用 readline() 可以每次读取一行内容，调 用 readlines() 一次读取所有内容并按行返回 list 。
因此，要根据需要决定怎么调用。

如果文件很小， read() 一次性读取最方便;如果不能确定文件大小，
反复调用 read(size) 比较保险;如果是配置 文件，调用 readlines() 最方便:

'''
# with open('/Users/Encore/Desktop/Python3.0/Python/io2.txt', 'r') as f1:
# 	print f1.read()


f1 = open('/Users/Encore/Desktop/Python3.0/Python/io2.txt', 'r') 

for line in f1.readlines():
	print(line.strip())  # 把末尾的'\n'删掉


'''
前面讲的默认都是读取文本文件，并且是ASCII编码的文本文件。要读取二进制文件，比如图片、视频等
等，用 'rb' 模式打开文件即可:
'''

#imageRB = open('/Users/Encore/Desktop/zp.png','rb') 
#print imageRB.read()

'''
字符编码 要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件:

如果每次都这么手动转换编码嫌麻烦(写程序怕麻烦是好事，不怕麻烦就会写出又长又难懂又没法维护的代码)，
P ython还 供了一个 codecs 模块帮我们在读文件时自动转换编码，直接读出unicode:

'''

'''
f = open('/Users/michael/gbk.txt', 'rb')

import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
      f.read() # u'\u6d4b\u8bd5'

 '''

'''

写文件
写文件和读文件是一样的，唯一区别是调用 open() 函数时，
传入标识符 'w' 或者 'wb' 表示写文本文件或写二进制 文件:
'''


f = open('/Users/Encore/Desktop/Python3.0/Python/io2.txt', 'w')

f.write('python 语法写入的')

f.close() 

'''
当我们写文件时，操作系统往往不 会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
只有调用 close() 方法时，操作系统才 保证把没有写入的数据全部写入磁盘。
忘记调用 close() 的后果是数据可能只写了一部分到磁盘，剩下的丢失 了。
所以，还是用 with 语句来得保险:

要写入特定编码的文本文件，请效仿 codecs 的示例，写入unicode，由 codecs 自动转换成指定编码。
'''
with open('/Users/Encore/Desktop/Python3.0/Python/io2.txt', 'w') as f:
	f.write("用with可以保证写入的内容会被保存到磁盘")

'''
小结
在Python中，文件读写是通过 open() 函数打开的文件对象完成的。使用 with 语句操作文件IO是个好习惯。
'''




