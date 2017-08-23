#! usr/bin/env python
# -*- coding: utf-8 -*-

'''
：输入三个整数x,y,z，请把这三个数由小到大输出。

'''

l = []
for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)
l.sort()
print l


'''
在此总结一下 sort 与 sorted 的区别

只要是可迭代对象都可以用sorted 

sorted(itrearble, cmp=None, key=None, reverse=False)，最后会将排序的结果放到一个新的列表中
'''

