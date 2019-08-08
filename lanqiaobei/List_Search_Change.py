import random
# 问题描述
# 　　给定某整数数组和某一整数b。要求删除数组中可以被b整除的所有元素，同时将该数组各元素按从小到大排序。
# 如果数组元素数值在A到Z的ASCII之间，替换为对应字母。元素个数不超过100，b在1至100之间。
# 输入格式
# 　　第一行为数组元素个数和整数b
# 　　第二行为数组各个元素
# 输出格式
# 　　按照要求输出
# 样例输入
# 7 2
# 77 11 66 22 44 33 55
# 样例输出
# 11 33  55 M


list_element = input("元素个数为：")
b = input("能够被b整除的b为：")
listnum = []
delnum = []
for i in range(int(list_element)):
	listnum.append(int(random.uniform(1,100)))

for j in range(len(listnum)-1,-1,-1): # !!!!!!!!!!!!!!很重要 从后面开始，因为从前面开始，[25, 60, 33, 70, 47, 20, 52]
										# j =  0 25 % 2 = 1
										# [25, 60, 33, 70, 47, 20, 52]
										# j =  1 60 % 2 = 0
										# [25, 33, 70, 47, 20, 52]
										# j =  2 70 % 2 = 0
										# [25, 33, 47, 20, 52]
										# j =  3 20 % 2 = 0
										# [25, 33, 47, 52]

	if listnum[j]%int(b) == 0:
		del(listnum[j])
listnum.sort()
for k in range(len(listnum)):
	if listnum[k]>=65 and listnum[k]<=90:
		listnum[k] = chr(listnum[k])

print(listnum)


