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
	returnMat = zeros((numerOfLines,3)) #创建一个 numerOfLines行 ，3列的二维数组（就是一个矩阵），0
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip() # 去掉末尾的换行符，
		listFromLine = line.split('\t') #split() 切割 \t代表是一个tab键值，就是8位，具体空格的个数，跟你的数值有关系，比如你的字符串是abc，加个\t，则空格是5个，如果字符串是abcde，加\t，则空格是3个
		returnMat[index,:] = listFromLine[0:3] #获取 0，1，2三个字符串元素 ,[index: ],表示到最大一个
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat,classLabelVector

datingDataMat, datingLabels = file2matrix("/Users/Encore/Desktop/Python3.0/Python/Machine_Learning/datingTestSet2.txt")

print datingDataMat

print datingLabels[0: 20]


fig = plt.figure()
ax = fig.add_subplot(111) #将画布分为1行1列，即一块大的，（349）表示将画布分3行4列共12块，9表示12块的第九块，即左下角那块
print type(ax)
ax.scatter(datingDataMat[:,1], datingDataMat[:, 2])
plt.show()