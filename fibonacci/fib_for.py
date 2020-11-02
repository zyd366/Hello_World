#!/usr/bin/env python
# coding: utf-8

# In[2]:


# -*- coding: UTF-8 -*-
#斐波那契数列   ## 写个函数最好了
n1 = 0 #定义第一项
n2 = 1 #定义第二项
for i in range(3, 100,1): #从第三项循环到第99项
	n3 = n1 + n2 #当前项等于前两项和
	print(n1,end=" , ") #输出斐波那契数列
	n1 = n2 #新的第一项等于原先的第二项
	n2 = n3 #新的第二项等于原先的第三项
