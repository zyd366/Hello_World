#!/usr/bin/env python
# coding: utf-8

# ## 导入CSV数据

# In[1]:


import numpy as np
import pandas as pd
from random import shuffle
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from pandas import set_option
from sklearn.preprocessing import StandardScaler #正态化数据
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV #网格优化搜索参数 模块
from sklearn.metrics import  accuracy_score      #准确率评分

from sklearn.pipeline import Pipeline            #自动化处理 函数
#分类算法 函数
from sklearn.linear_model import LogisticRegression#导入逻辑回归模型
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB       #符合高斯分布的朴素贝叶斯
from sklearn.svm import SVC
diab=pd.read_csv(r'C:\Users\dell\Desktop\Python_project\ZYD366\diabetes.csv')
names = {'Pregnancies':'preg','DiabetesPedigreeFunction':'DPF',
         'BloodPressure':'pres','SkinThickness':'skin','Outcome':'class'}
diab.rename(columns = names, inplace = True)     #重命名列
diab_1 = diab.copy()                             #建立数据副本
print(round(diab.describe().T,3))                #print数据的描述统计量
diab


# ## 删除异常值

# In[3]:


diab = diab.drop(diab[diab.Glucose==0].index)
diab = diab.drop(diab[diab.pres==0].index)
diab


# ## 检查数据中是否存在缺失值

# In[4]:


diab.isnull().any(axis=0)    #检查数据中是否存在缺失值


# ## 数据可视化

# In[5]:


diab.hist(figsize=(16,10))#可视化（定义长宽）
plt.show()


# In[6]:


import seaborn as sns
print(diab_1.shape)
sns.pairplot(diab_1,vars=diab_1.columns[:-1],hue='class')#建立散点矩阵
plt.show()


# ## 建立训练数据集

# In[7]:


array = diab.values  # 获取值
X = array[:, 0:8]  # 读取下标从0-7列的数据 
print(X)
Y = array[:, 8]  # 读取列下标所在行数据
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,random_state = 7)


# ## 评估算法的基准

# In[8]:


num_fold = 10
seed = 7
scoring = 'accuracy'


# ## 创建模型字典并实例

# In[9]:


modes = {}
modes['LR'] = LogisticRegression()
modes['KNN'] = KNeighborsClassifier()
modes['Tree'] = DecisionTreeClassifier()
modes['NB'] = GaussianNB()
modes['SVM'] = SVC()


# In[10]:


results = []
for key in modes:
    kfold = KFold(n_splits=num_fold,random_state=seed)
    cv_results = cross_val_score(modes[key],X_train,Y_train,cv=kfold,scoring=scoring)
    results.append(cv_results)
    print('{0}算法{1:.2%},标准方差:{2:.2f}'.format(key,cv_results.mean(),cv_results.std()))


# ## 算法参数调参

# In[11]:


#(网格搜索优化参数、随机搜索优化参数)
#KNN算法调参
scaler = StandardScaler().fit(X_train)
rescalerX = scaler.transform(X_train)
param_grid = {'n_neighbors':[1,3,5,7,9,11,13,15,17,19,21,22]}
model = KNeighborsClassifier()
kfold = KFold(n_splits=num_fold,random_state=seed)
grid = GridSearchCV(estimator=model,param_grid=param_grid,scoring=scoring,cv=kfold)
grid_reslut = grid.fit(X=rescalerX,y=Y_train)

print("最好模型准确率：{0:.2%},参数是：{1}".format(grid_reslut.best_score_,grid_reslut.best_params_))

cv_results = zip(grid_reslut.cv_results_['mean_test_score'],
grid_reslut.cv_results_['std_test_score'],
grid_reslut.cv_results_['params'])

for mean,std,param in cv_results:
    print('算法准确率{0:.2%},标准方差:{1:.2f},参数:{2}'.format(mean,std,param))


# In[12]:


#支持向量机调参（C（惩罚系数）、kernel内核函数）
scaler = StandardScaler().fit(X_train)

rescalerX = scaler.transform(X_train).astype(float)
param_grid = {}

param_grid['C'] = [0.1,0.2,0.3,0.4,0.5,0.7,0.9,1.0,1.3,1.5,1.7,2.0]
param_grid['kernel'] = ['linear','poly','rbf','sigmoid']

model = SVC()

kflod = KFold(n_splits=num_fold,random_state=seed)
grid = GridSearchCV(estimator=model,param_grid=param_grid,scoring=scoring,cv=kflod)

grid_reslut = grid.fit(X=rescalerX,y=Y_train)

print('最优的准确率：{0:.2%},最优的参数:{1}'.format(grid_reslut.best_score_,grid_reslut.best_params_))

cv_results = zip(grid_reslut.cv_results_['mean_test_score'],
grid_reslut.cv_results_['std_test_score'],
grid_reslut.cv_results_['params'])

for mean,std,param in cv_results:
    print('准确率:{0:.2%},标准方差:{1:.2f},参数:{2}'.format(mean,std,param))


# ## 确定最终模型

# In[14]:


scaler = StandardScaler().fit(X_train)
rescalerX = scaler.transform(X_train)
model = SVC(C=0.7,kernel='linear')
model.fit(X=rescalerX,y=Y_train)

#评估模型（验证集数据）
rescaler_test_X = scaler.transform(X_test)
predictions = model.predict(rescaler_test_X)
print('准确率：{0}'.format(accuracy_score(Y_test,predictions)))
print(confusion_matrix(Y_test,predictions))
print(classification_report(Y_test,predictions))

