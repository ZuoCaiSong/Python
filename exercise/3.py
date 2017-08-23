#! usr/bin/env python
# -*- coding: utf-8 -*-

'''
计算两个变量的值
i*j = 168 , j>=2, 则 1<i < 168/2 + 1

'''

for i in range(1, 85):
	if 168 % i == 0:
		j = 168/i
		if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
			m = (i + j)/2
			n = (i - j)/2
			print pow(n,2) - 100
