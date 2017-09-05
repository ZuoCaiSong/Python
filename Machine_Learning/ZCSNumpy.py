#! usr/bin/env python
# -*- coding:utf-8 -*-

"""
基础篇
"""
from numpy  import *

'''
NumPy的主要对象是同种元素的多维数组。
这是一个所有的元素都是一种类型、通过一个正整数元组索引的元素表格(通常是元素是数字)
'''

'''
NumPy中维度(dimensions)叫做轴(axes)，轴的个数叫做秩(rank)。
'''
#eg:
'''
在3D空间一个点的坐标 [1,2,3]
是一个秩为1的数组，它只有一个轴，轴的长度为3
'''
#注意直接写，他的类型不是一个ndarray，是一个list，此处只是用于举例说明秩
arr2 = [[1,0,0],
		[0,1,0]]
'''
arr2 的秩为2 (它有两个维度)
'''

'''
NumPy的数组类被称作 ndarray 。通常被称作数组。
注意numpy.array和标准python库类array.array并不相同，
后者只处理一维数组和提供少量功能
'''

# 创建一个numpy的对象
a = arange(15).reshape(3, 5)
print a

# 数组轴的个数（秩），行数
print "a的秩为", a.ndim

help(ndim)