from time import *
import random
from datetime import datetime,date,time
import time

tickets=[
	['2018-4-7 8:00','北京','沈阳',10,120],
	['2018-4-7 9:00', '上海', '宁波', 5, 100],
	['2018-4-7 12:00', '天津', '北京', 20, 55],
	['2018-4-7 14:00', '广州', '武汉', 0, 200],
	['2018-4-7 16:00', '重庆', '西安', 3, 180],
	['2018-4-7 18:00', '深圳', '上海', 49, 780],
	['2018-4-7 18:00', '武汉', '长沙', 10, 210],
] # 出发时间 出发站 终点站 数量 价格

tickets2=[
	['2018-4-7 8:00','北京','沈阳',10000,120],
	['2018-4-7 9:00', '上海', '宁波', 6000, 100],
	['2018-4-7 12:00', '天津', '北京', 20000, 55],
	['2018-4-7 14:00', '广州', '武汉', 5110, 200],
	['2018-4-7 16:00', '重庆', '西安', 8000, 180],
	['2018-4-7 18:00', '深圳', '上海', 6900, 780],
	['2018-4-7 18:00', '武汉', '长沙', 7000, 210],
]
def buy_ticket(name,nums,date1,start_station):
	i = 0
	sleep(1)
	# for get_record in tickets:
	for get_record in tickets:
		if get_record[0]==date1 and get_record[1] == start_station:
			if get_record[3]>=nums:
				# tickets[i][3] = get_record[3]-nums
				tickets[i][3] = get_record[3] - nums
				print("%s购买%d张票成功！" % (name, nums))
				return nums
			else:
				print('%s现在存票数量不够，无法购买！'%(name))
				return -1
		i+=1
	print("%s今日无票，无法购买！"%(name))
	return -1

def buy_ticket2(name,nums,date1,start_station):
	i = 0
	sleep(1)
	# for get_record in tickets:
	for get_record in tickets2:
		if get_record[0]==date1 and get_record[1] == start_station:
			if get_record[3]>=nums:
				# tickets[i][3] = get_record[3]-nums
				tickets2[i][3] = get_record[3] - nums
				print("%s购买%s,%s,%d张票成功！"%(name,date1,start_station,nums))
				return nums
			else:
				print('%s现在存票数量不够，无法购买！'%(name))
				return -1
		i+=1
	print("%s今日无票，无法购买！"%(name))
	return -1


if __name__=='__main__':
	print('开始时间',datetime.now())
	d1 = datetime.now()
	# result = buy_ticket('张三',3,'2018-4-7 9:00','上海')
	# if result>0:
	# 	print("张三购买%d张票成功！"%(3))
	# result = buy_ticket('李四',1,'2018-4-7 14:00','广州')
	# if result>0:
	# 	print("李四购买%d张票成功！"%(1))
	# result = buy_ticket('王五',2,'2018-4-7 9:00','上海')
	# if result>0:
	# 	print("王五购买%d张票成功！"%(2))
	name = []
	nums = []
	date1 = []
	start_station = []
	for i in range(0,100):
		name.append("customer%d"%(i))
		nums.append(int(random.uniform(0,5)))
		wherestart  = int(random.uniform(0,7))
		date1.append(tickets2[wherestart][0])
		start_station.append(tickets2[wherestart][1])
	for j in range(0,100):
		result = buy_ticket2(name[j],nums[j],date1[j],start_station[j])
		if result > 0:
			print("%s购买%d张票成功！"%(name[j],nums[j]))


	print("结束时间",datetime.now())
	d2 = datetime.now()
	print("用时：",d2-d1)
	print("剩余票数为：\n")
	for gets in tickets2:
		print(gets)
