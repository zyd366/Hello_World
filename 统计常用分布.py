#!/usr/bin/env python
# coding: utf-8

# In[43]:

import scipy.stats as st
from scipy.stats import binom    #伯努利试验
import seaborn as sns
data_binom = binom.rvs(n=1,p=0.5,size=10000) #定义分布的参数，并生成随机数（下同）
print(st.describe(data_binom))	#输出此分步的一系列统计指标如值域、均值、方差、偏度、峰度等
ax = sns.distplot(data_binom,
                  kde=False,    #不需要线图
                  color='pink', 
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')#定义图像的坐标轴
print(data_binom)


# In[95]:


from scipy.stats import binom    #二项分布
data_binom = binom.rvs(n=10,p=0.5,size=100000)
print(st.describe(data_binom))	 #输出此分步的一系列统计指标如值域、均值、方差、偏度、峰度等
ax = sns.distplot(data_binom,
                  kde=False,
                  color='cyan',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')
print(data_binom)


# In[94]:


from scipy.stats import geom    #几何分布
data_geom = geom.rvs(size=100000,p=0.5)
print(st.describe(data_geom))
ax= sns.distplot(data_geom,
                 kde=False,
                 color="purple",
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Geometric Distribution', ylabel='Frequency')
print(data_geom)


# In[102]:


from scipy.stats import poisson    #泊松分布
data_poisson = poisson.rvs(mu=2, size=100000)
print(st.describe(data_poission))
ax = sns.distplot(data_poisson,
                  bins=30,
                  kde=False,
                  color="blue",
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')
print(data_poisson)


# In[45]:


from scipy.stats import norm    #正态分布
# 生成标准正态分布，N(0,1)
data_normal = norm.rvs(size=100000,loc=0,scale=1)
print(st.describe(data_normal))  
ax = sns.distplot(data_normal,
                  bins=100,     #定义箱子的个数
                  kde=True,     #绘制线图
                  color="purple",
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
print(data_normal)


# In[100]:


from scipy.stats import expon    #指数分布
expon_normal = expon.rvs(5,size=100000)
print(st.describe(expon_normal))
ax = sns.distplot(expon_normal,
                  bins=100,
                  kde=True,
                  color="purple",
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Expon Distribution', ylabel='Frequency')
print(expon_normal)


# In[99]:


from scipy.stats import chi2    #卡方分布
chi2_normal = chi2.rvs(15,size=100000)
print(st.describe(chi2_normal))
ax = sns.distplot(chi2_normal,
                  bins=100,
                  kde=True,
                  color="purple",
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Chi2 Distribution', ylabel='Frequency')
print(chi2_normal)


# In[98]:


from scipy.stats import t    #卡方分布
t_normal = t.rvs(15,size=100000)
print(st.describe(t_normal))
ax = sns.distplot(t_normal,
                  bins=100,
                  kde=True,
                  color="purple",
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='T Distribution', ylabel='Frequency')
print(t_normal)


# In[109]:


from scipy.stats import f     # F分布
f_normal = f.rvs(5,18,size=100000)
print(st.describe(f_normal))
ax = sns.distplot(f_normal,
                  bins=100,
                  kde=True,
                  color="purple",
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='F Distribution', ylabel='Frequency')
print(f_normal)


# In[ ]:




