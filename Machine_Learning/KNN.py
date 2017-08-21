#! usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import operator # 运算符模块
def createDataSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0,0], [0, 0.1]]) #Numpy库中的矩阵模块为ndarray对象
	labels = ['A', 'A', 'B', 'B']
	print type(group) #<type 'numpy.ndarray'>
	return group, labels

'''
inX: 做分类的输入向量
dataSet: 输入的训练样本集 ,为 numpy中的ndarray类型 即为矩阵类型
labels: 标签向量 （元素数目等于矩阵dataset的行数）
K: 用于表示选择最近邻居的数目 
'''

def classify0(inX, dataSet, labels, k):
	dataSetSize  = dataSet.shape[0] # dataSet为一个二维数组，shape 求数组的行数，与列数为一个tupe

	#前面用tile，把一行inX变成4行一模一样的（tile有重复的功能，以dataSetSize行1列重复）
	#，然后再减去dataSet，是为了求两点的距离，先要坐标相减，这个就是坐标相减
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet 
	print diffMat 
	sqDiffMat = diffMat ** 2 #上一行得到了坐标相减，然后这里要(x1-x2)^2，要求乘方 
	print sqDiffMat 
	sqDistances = sqDiffMat.sum(axis=1)  #axis=1每一行相加，相加的结果在组成一个新的结果，array([1, 2]), 则不能用sum(axis=1),只能用sum()，这样得到了(x1-x2)^2+(y1-y2)^2  
	distances = sqDistances ** 0.5   #开根号，这个之后才是距离
	print "---------------9" 
	print distances 
	sortedDistIndicites = distances.argsort() #argsort是排序，将元素按照由小到大的顺序返回下标，比如([3,1,2]),它返回的就是([1,2,0])
	print sortedDistIndicites
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicites[i]]  # sortedDistIndicites[i] 取到前面K个最小元素的值所对应的下标

		#get是取字典里的元素，如果之前这个voteIlabel是有的，那么就返回字典里这个voteIlabel里的值，如果没有就返回0（后面写的），
		#这行代码的意思就是算离目标点距离最近的k个点的类别，这个点是哪个类别哪个类别就加1
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 

	 #key=operator.itemgetter(1)的意思是按照字典里的第一个排序，{A:1,B:2},要按照第1个（AB是第0个），即‘1’‘2’排序。reverse=True是降序排序 	
	'''
	operator这个模块中的两个函数：
    1）itemgetter
    operator.itemgetter(item)
    operator.itemgetter(*items)
	'''
	sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True)  #降序,返回的是一个数组字典
	print "---------------9" 
	print sortedClassCount
	return sortedClassCount[0][0]  #返回类别最多的类别 ,

group , labels = createDataSet()

print type(group.shape) #获取矩阵的行列 结果为 (4, 2)

print classify0([0,0], group, labels, 3)




def classify1(inX, dataSet, labels, k):
	dataSetSize  = dataSet.shape[0] # dataSet为一个二维数组，shape 求数组的行数，与列数为一个tupe

	#前面用tile，把一行inX变成4行一模一样的（tile有重复的功能，以dataSetSize行1列重复）
	#，然后再减去dataSet，是为了求两点的距离，先要坐标相减，这个就是坐标相减
	diffMat = tile(inX, (dataSetSize, 2)) #- dataSet 
	print diffMat

group , labels = createDataSet()
classify1([1,2], group, labels, 3)

a = array([[1, 2,7,3], [3, 5,4,2]])

s = a.argsort() 
print "---------------------------"
print (s)
print a





