# 问题描述
# 　　“两只小蜜蜂呀，飞在花丛中呀……”
# 　　话说这天天上飞舞着两只蜜蜂，它们在跳一种奇怪的舞蹈。用一个空间直角坐标系来描述这个世界，那么这两只蜜蜂初始坐标
# 分别为(x1,y1,z1)，(x2,y2,z2)　　。
# 在接下来它们将进行n次飞行，第i次飞行两只蜜蜂分别按照各自的速度向量飞行ti个单位时间。
# 对于这一现象，玮玮已经观察了很久。他很想知道在蜜蜂飞舞结束时，
# 两只蜜蜂的距离是多少。现在他就求教于你，
# 请你写一个程序来帮他计算这个结果。
#
# 输入格式
# 　　第一行有且仅有一个整数n，表示两只蜜蜂将进行n次飞行。
#  　　接下来有n行。
#  　　第i行有7个用空格分隔开的整数ai,bi,ci,di,ei,fi,ti　　，表示第一只蜜蜂单位时间的速度向量为(ai,bi,ci) ，
# 	第二只蜜蜂单位时间的速度向量为(di,ei,fi) ，它们飞行的时间为ti 。
#  　　最后一行有6个用空格分隔开的整数x1,y1,z1,x2,y2,z2，如题所示表示两只蜜蜂的初始坐标。
# 输出格式
# 　　输出仅包含一行，表示最后两只蜜蜂之间的距离。保留4位小数位。
# 样例输入
# Sample 1
# 1
# 1 1 1 1 -1 1 2
# 3 0 1 2 0 0
# Sample 2
# 3
# 1 1 1 1 -1 1 2
# 2 1 2 0 -1 -1 2
# 2 0 0 -1 1 1 3
# 3 0 1 2 0 0
#
# 样例输出
# Sample 1
# 4.2426
# Sample 2
# 15.3948
import math
def countfly(fly):
	B1x = 0
	B1y = 0
	B1z = 0
	B2x = 0
	B2y = 0
	B2z = 0
	for i in range(len(fly)):
		ai, bi, ci, di, ei, fi, ti = fly[i]
		B1x = B1x + ai * ti
		B1y = B1y + bi * ti
		B1z = B1z + ci * ti
		B2x = B2x + di * ti
		B2y = B2y + ei * ti
		B2z = B2z + fi * ti
	return B1x,B1y,B1z,B2x,B2y,B2z

n = input("蜜蜂飞行n次，n = ")
fly = []
firstpoint = [0,0,0,0,0,0]
for i in range(int(n)):
	fly.append(map(float,input("蜜蜂第%d次飞行的速度向量以及时间为：[ai,bi,ci,di,ei,fi,ti] = "%(i+1)).split()))
x1,y1,z1,x2,y2,z2 = map(float,input("蜜蜂初始位置为：[x1,y1,z1,x2,y2,z2] = ").split())
B1x,B1y,B1z,B2x,B2y,B2z = countfly(fly)
Bee1_x = x1+B1x
Bee1_y = y1+B1y
Bee1_z = z1+B1z
Bee2_x = x2+B2x
Bee2_y = y2+B2y
Bee2_z = z2+B2z
juli = math.sqrt((Bee1_x- Bee2_x)**2+(Bee1_y- Bee2_y)**2+(Bee1_z- Bee2_z)**2)
print("距离为%.4f"%(juli))

