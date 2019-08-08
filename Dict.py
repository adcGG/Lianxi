# 是可变的无序集合，同时是一种以键值对为基本元素的可以存储各种数据类型的集合，用 大括号 表示字典的开始和结束，元素之间用 逗号
#  隔开
# 键值对 由 键 和 值 组成，中间由 冒号 隔开，实现了紧密的一对一关系，从键值对可以看出，字典属于典型的一对一 映射关系的数据类型
# 一个字典对象里边 所有的键 必须唯一。如果相同或不同 保存 键相同的最后一个元素。
# 字典有不可变性
#
d1 = {'Tom':2,
      'Jim':5}
d1['Mike'] = 7
print(d1)

d1.setdefault('Alice',10) # 逗号
d1.setdefault('Tim')
print(d1)
print(d1['Tom'],d1.get('Alice'))
print('ssss',d1.get('ff'),type(d1.get('ff')))

# 修改
d1['Tom'] = 12
d1.update({'Green':16})
d2 = {'Mike':34,'Tim':36,'Wang':9}
d1.update(d2)
print(d1)

# 删除
del(d1['Jim'])
print(d1)
d1 = {'Tom': 12, 'Mike': 34, 'Alice': 10, 'Tim': 36, 'Wang': 9, 'Green': 16}
p1 = d1.pop('Mike') # 返回值
print(p1,d1)

t1 = d1.popitem() # 随机删除并返回一个 元组格式的 键值对 ,删除最后一个
print(t1,type(t1))

# 遍历。items会以元组的形式返回字典所有元素
d1 = {'Tom': 12, 'Mike': 34, 'Alice': 10, 'Tim': 36, 'Wang': 9, 'Green': 16}
for get_L in d1.items():
	print(get_L)
dict_items = d1.items()
print(dict_items,type(dict_items))

# 遍历所有键
for gets in d1:
	print(gets)
for gets1 in d1.keys():
	print(gets1)

# 遍历所有值
for get_key in d1:
	print(d1[get_key])
for get_v in d1.values():
	print(get_v)

# 通过copy()的方式复制 可以避免字典变量之间直接复制指向同一个地址的问题
d2 = d1
d3 = d1.copy()
print(id(d1),id(d2),id(d3))

# fromkeys()方法只能给字典增加键而对应的值为空的特点
d4 = {}.fromkeys(['pen','rule','paper'])
print(d4)
