# 问题描述
# 　　给定N个物品,每个物品有一个重量W和一个价值V.你有一个能装M重量的背包.问怎么装使得所装价值最大.每个物品只有一个.
# 输入格式
# 　　输入的第一行包含两个整数n, m，分别表示物品的个数和背包能装重量。
#  　　以后N行每行两个数Wi和Vi,表示物品的重量和价值
# 输出格式
# 　输出1行，包含一个整数，表示最大价值。
# 样例输入
# 3 5
#  2 3
#  3 5
#  4 7
# 样例输出
# 8
# 数据规模和约定
# 　　1<=N<=200,M<=5000.
import random
# n,m=map(int,input("输入两个整数n, m，分别表示物品的个数和背包能装重量：\n").split())
n = int(random.uniform(5,15))
m = int(random.uniform(10,30))
print("输入两个整数n, m，分别表示物品的个数和背包能装重量：\n",n,m)
wi = []
vi = []
for i in range(n):
	# a,b=map(int,input("第%d个，物品的重量和价值："%(i+1)).split())
	a = int(random.uniform(8,25))
	b = int(random.uniform(5,30))
	wi.append(a)
	vi.append(b)
print("wi:",wi,"vi:",vi)
index = []
for j in range(n):
	if wi[j]>m:
		index.append(wi.index(wi[j]))
print('index:',index)
for i in range(len(index)-1,-1,-1):
	print("i",i,"删除:",wi[index[i]])
	wi.remove(wi[index[i]])
	vi.remove(vi[index[i]])


print("wi:",wi,"vi:",vi)

