#! usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import *
import operator
import  matplotlib
import  matplotlib.pyplot as plt
'''
r：读
rb： 读二进制文件
'''
def file2matrix(fileName):
	fr = open(fileName)
	arrayOLines = fr.readlines() #用 readlines() 一次读取所有内容并按行返回 list 
	numerOfLines = len(arrayOLines) #行数
	returnMat = zeros((numerOfLines,3)) #创建一个 numerOfLines行 ，3列的二维数组（就是一个矩阵），
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip() # 去掉末尾的换行符，
		listFromLine = line.split('\t') #split() 函数，可以把一个路径拆分为 两部分，后一部分总是最后级别的目录或文件名 /a/b/c.txt  ==>('/a/b', 'c.txt')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat,classLabelVector

datingDataMat, datingLabels = file2matrix("/Users/Encore/Desktop/Python3.0/Machine_Learning/datingTestSet2.txt")

print datingDataMat

print datingLabels[0: 20]


fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:, 2])
plt.show()