#!/usr/bin/env python
# coding: utf-8

# In[32]:


n = int(input("请输入你所需要的项数：\n"))
def fib(n):
    if n == 1 :
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(1, n+1 ,1):
    print(frog(i),end=",")


# In[ ]:




