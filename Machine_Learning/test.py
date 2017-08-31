#! usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import operator
import  matplotlib
import  matplotlib.pyplot as plt


def file1(filname):
	fr = open(filname)
	arrLins = fr.readlines()
	for line in arrLins:
		print (line)
		line = line.strip()
		print (line)
		listF = line.split('\t')
		#str.split(str="", num=string.count(str)).
	    #如果参数num 有指定值，则仅分隔 num 个子字符串. 返回分割后的字符串列表。
		# print type(listF)
		print listF


#file1("/Users/Encore/Desktop/Python3.0/Python/Machine_Learning/datingTestSet2.txt")

#一维数组，全是0 zeros(3)  

#二维数组 zeros([3,3]), zeros((3,3)
returnMat = zeros((3,3))
print returnMat
l = ["1","2","3","4"]
returnMat[0,:] = l[0:3]
print returnMat
