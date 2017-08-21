#! usr/bin/env python
# -*- coding:utf-8 -*-

d = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                d.append([i,j,k])
print "总数量：", len(d)
 


# 将for循环和if语句综合成一句，直接打印出结果 
list_num = [1,2,3,4]

list = [i*100 + j*10 + k for i in list_num for j in list_num for k in list_num if (j != i and k != j and k != i)]   

print (list)          