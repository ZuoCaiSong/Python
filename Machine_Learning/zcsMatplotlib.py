#! usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-1,1,50)
y1 = 2*x + 1
y2 = x**2

plt.figure(num = 1)
plt.plot(x,y1)


plt.figure(num = "zcs", figsize=(8,5)) # num = 3 表示为figure3 ，figsize 表示图片的大小

# 对X，y轴进行相关的设置

"""
1.对X，y轴进行可见范围的限制设置
"""
plt.xlim((-1,2))
plt.ylim((-2,3))

'''
设置x,y轴代表的含义
'''

plt.xlabel('i am x')
plt.ylabel('i am y')

'''
ticks,修改x轴的步进
'''
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)

# 让y在特殊的值上，打印特殊的状态
plt.yticks([-2,-1.8,-1, 1.22,3],
			[r'$really\ bads$', r'$bad$', r'$normal$', '$good$', 'really good']) #前后两个$表示改为好看的字体，r表示正则，在正则下空格需要\转义




'''
平移坐标轴
gca = 'get current axis' #获得当前的轴
'''

ax = plt.gca()
# spines 为figure的四条边框，默认是四条实线
ax.spines['right'].set_color('none') # 右边的实线颜色为none，无色
ax.spines['top'].set_color('none') #top的实线

ax.xaxis.set_ticks_position('bottom') # xaxis:axis表示轴，前面加个x表示X轴，将bottom设为x轴
ax.yaxis.set_ticks_position('left') # xaxis:axis表示轴，前面加个y表示Y轴，将left设为x轴



ax.spines['bottom'].set_position(('data',0)) #移动bottom ,即x轴，设置x轴的位置为 y轴的值（data)为0的横线，作为x轴
ax.spines['left'].set_position(('data',0))  #移动left,即y轴，设置y轴的位置为 x轴的值（data)为0的竖直线，作为y轴

l1, = plt.plot(x,y2,label = 'up') #label是用于下面绘制图例使用 ，每个都有返回值，返回"线“的实例，如果要放入参数handles，则返回值后面加一个,
l2, = plt.plot(x,y1, color = 'red', linewidth = 1.0, linestyle = '--', label = 'down') #红色、线宽、虚线


'''
制作图例，1.在plot中使用关键字label，给每个图形打一个标签 ,见上
2. 让图例显示出来调用代码：legend
'''
#plt.legend(handles = [l1,l2,] , labels = ['y = 2*x + 1', 'y = x**2'], loc = 'best') # loc 自动找一个合适的位置，数据比较小，不集中的地方

plt.legend(handles = [l1,l2,], labels = ['aaa','bbb'], loc = 'best') 


plt.show()















