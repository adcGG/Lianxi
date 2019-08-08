from FishStat_M import *
d_data1 = {'鲫鱼':[17,10.5],'鲤鱼':[8,6.2],'鲢鱼':[7,4.7]}
d_data2 = {'草鱼':[2,7.2],'鲫鱼':[3,12],'黑鱼':[6,15]}
d_data3 = {'乌龟':[1,78.10],'鲫鱼':[1,10.78],'草鱼':[5,7.92]}
fish_records = {'1月1日':d_data1,'1月2日':d_data2,'1月3日':d_data3}

print('===========鱼 每日统计==================')
for day,day_record in fish_records.items():
	day_stat(day,day_record)

print('===========鱼 所有数量统计==============')
name1 = ""
maxstat = ['',0,'',0,0,0]
all_stat = allday_stat(fish_records,maxstat)

for name1,subs in all_stat.items():
	print('%s 数量 %d 金额 %.2f'%(name1,subs[0],subs[1]))

print('\n '
      '==========最大值，总数量，总金额打印===')
PrintMaxValues(maxstat)