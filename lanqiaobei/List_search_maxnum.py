import random
# 问题描述
# 　　对于给定整数数组a[],寻找其中最大值，并返回下标。
# 输入格式
# 　　整数数组a[],数组元素个数小于1等于100。输出数据分作两行：第一行只有一个数，表示数组元素个数；第二行为数组的各个元素。
# 输出格式
# 　　输出最大值，及其下标
# 样例输入
# 3
# 3 2 1
# 样例输出
# 3 0

n = input("数组元素的个数：")
a = []
for i in range(int(n)):
	a.append(int(random.uniform(1,100)))
print(a)
maxnum = max(a)
num = a.index(maxnum)
print(maxnum,num)