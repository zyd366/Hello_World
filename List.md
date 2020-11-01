# Python列表
## 1 列表定义
在python中列表是用符号[]来表示，并用逗号来分隔其中的元素，当引用列表内的元素时，索引从0开始，引用最后一个元素可以用[-1]来表示。
比如：
```pyhon
// FileName: list.python
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[1])     #打印第二项cannondale
print(bicycles[-1])    #打印最后一项specialized
```

## 2 列表使用和修改
列表中各个值的使用和修改都需要先索引，然后将其当作变量处理。并且列表与字符的拼接和变量相同，列表内的元素修改类似变量重新赋值。
```pyhon
// FileName: listuse.python
bicycles = ['trek','cannondale','redline','specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)          #输出My first bicycle was a Trek.
bicycles[0] = 'fenghuang'
print(bicycles[0])      #打印出修改后的列表第一项
```
## 3 添加元素
在Python中，列表中元素的添加方式有两种，一种是添加到列表末尾使用方法append()；还一种是将元素插入到指定位置，使用方法insert()，此时需制定新元素的索引和值。具体情况如下：
```pyhon
// FileName: listchange.python
bicycles = ['trek','cannondale','redline']
print(bicycles)             #打印原列表用于对照
bicycles.append('bike')     #在列表末尾添加元素bike
bicycles.insert(1,'ducati') #在列表的第二项插入元素ducati
print(bicycles)             #打印出修改后的列表['trek','ducati','cannondale','redline','bike']
```
## 4 删除元素
列表内的元素删减可以使用del 如：del bicyles[0]或者使用方法pop()、remove（）。其不同点在于del语句将值从列表中删除后，你就无法访问删除的值，而pop()删除列表末尾的值该值后仍可使用；remove则是根据所删除的值进行删除。其具体表现如下：
```pyhon
// FileName: listdel.python
bicycles = ['trek','cannondale','redline','bike']
print(bicycles)             #打印原列表用于对照
del bicycles[1]             #删除列表内的第二个元素cannondale
print(bicycles)             
popped_bicycle = bicycles.pop()    #删除列表末尾的元素bike并将其值赋给变量popped_bicycle
print(bicycles)             #打印删除末尾元素后的列表
print(popped_bicycle)
bicycles.remove('redline')  #根据元素值删除列表元素redline
print(bicycles)             #打印出修改后的列表['trek']
```
## 5 组织列表
在Python中，方法sort()可以使列表内的元素按字母顺序排列，并且是永久性修改不可恢复；如要按与字母顺序相反的顺序排列列表元素可以用“列表名.sort(reverse=Ture)”的形式进行排序；临时排序可用sorted函数，如：print(sorted(cars))；倒着打印列表使用方法.reverse()，即反转列表元素的排列顺序，用法如同.sort()。如：travel.reverse()。
```pyhon
// FileName: listsort.python
bicycles = ['trek','cannondale','redline','bike']
bicycles.sort()             #将bicycle列表按字母顺序排序
print(bicycles)             
bicycles = ['trek','cannondale','redline','bike']
bicycles.sort(reverse=True) #将列表按与字母顺序相反的循序排序
print(bicycles)
bicycles = ['trek','cannondale','redline','bike']
print(sorted(bicycles))     #按字母顺序打印列表，此时为临时排序
bicycles = ['trek','cannondale','redline','bike']
bicycles.reverse()          #将列表的与按顺序反转
print(bicycles)
```
## 6 确定列表长度
在Python中可以通过方法len()来计算列表的长度。
如：
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
```
# 列表与元组的区别
列表和元组的区别大致可以分为三点：
首先，元组看起来很像列表，但它是使用圆括号而不是方括号标识；其次，列表中的值是可以修改的，而元组的值是不能修改的；最后，元组可以在映射（和集合的成员）中当做“键”使用，而列表不行。
需要注意的是尽管元组的元素不能修改，但我们可以给存储元组的变量赋值。
