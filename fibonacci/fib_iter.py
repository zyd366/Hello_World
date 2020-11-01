#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Fibonacci(object):	#斐波那契数列迭代器
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):		#迭代器返回自身
        return self

    def __next__(self):
        if self.current_num < self.all_num:  # 判断是否可以迭代
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration  # 迭代完成，抛出异常，退出迭代


fib = Fibonacci(50)
for num in fib:
    print(num,end=",")


# In[ ]:




