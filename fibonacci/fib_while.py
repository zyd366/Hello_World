#!/usr/bin/env python
# coding: utf-8

# In[30]:

#斐波那契数列
n1 = 0  #定义第一项为0
n2 = 1  #定义第二项为1

i = input("请输入你需要的项数:\n") # 获取用户所需要的数列项数
if i.isnumeric():# 判断输入的值是否符合代码逻辑
    i = int(i)
    if i <=0:
        print("无效值，请重新输入:")
    else:
        count = 0
        while count < i:
            n3 = n1 + n2
            print (n1, end = ",")
            n1 = n2       # 更新值
            n2 = n3
            count = count + 1
else:
    print("请输入有效正整数")


# In[ ]:




