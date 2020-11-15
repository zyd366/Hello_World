#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def transform(one_num):
    '''
    将阿拉伯数字转化为罗马数字
    '''
    num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res=''
    for i in range(len(num_list)):
        while one_num>=num_list[i]:
            one_num-=num_list[i]
            res+=str_list[i]
    return res
while 1:
    one_num = input("请输入你想转化的数字:")
    if one_num == 'quit':#输入quit结束游戏#
        break
    elif one_num.isnumeric():     #判断是否为数字
        number = int(one_num)
        print(number,'----->',transform(number))
    else:
        print("请输入有效正整数字。")


# In[ ]:




