def day_stat(day,fishs):
	'''

	:param day: 为字符串参数
	:param fishs: 为两层嵌套字典参数
	:return:
	'''
	nums = 0
	amount = 0
	for name0,sub_records in fishs.items():
		print('%s 数量 %d 单价%.2f元'%(name0,sub_records[0],sub_records[1]))
		nums+=sub_records[0]
		amount += sub_records[0]*sub_records[1]
	print('%s 数量小计%d金额小计%.2f'%(day,nums,amount))

def allday_stat(fish,maxs):
	'''
	统计所有鱼，并保存到统计字典里
	:param fish: 为两层嵌套字典参数
	:return:
	'''
	name1 = ""
	sub_record = {}
	stat_record = {}
	for day,day_record in fish.items():
		for name1,sub_record in day_record.items():
			if name1 in stat_record:
				stat_record[name1][0]+=sub_record[0]
				stat_record[name1][1] += sub_record[0]*sub_record[1]
			else:
				stat_record[name1] = [sub_record[0],sub_record[0]*sub_record[1]]
	for name1,nums in stat_record.items():
		if maxs[1] < nums[0]:
			maxs[0] = name1
			maxs[1] = nums[0]
		if maxs[3] <nums[1]:
			maxs[2] = name1
			maxs[3] = nums[1]
		maxs[4] = maxs[4]+nums[0]
		maxs[5] = maxs[5]+nums[1]
	return stat_record


def PrintMaxValues(maxstat1):
	'''
	打印最大值
	:param maxstat1:[:4]为列表参数，记录最大值。[4]记录总数量 。 [5]记录总金额
	:return:
	'''
	print('最大数量的鱼是%s,%d条'%(maxstat1[0],maxstat1[1]))
	print('最大金额的鱼是%s,%.2f元'%(maxstat1[2],maxstat1[3]))
	print('钓鱼总数量为%d，总金额为%.2f元'%(maxstat1[4],maxstat1[5]))
