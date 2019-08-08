Name = ['张力','丁玲','毛小','王刚','李云']
buyObject = ('笔记本电脑','U盘','耳麦')
everyoneMoney = []
buyRecords = ['张力',buyObject,1,1,1,5000,123,500,
              '丁玲',buyObject,1,1,1,5000,123,100,
              '毛小',buyObject,1,1,1,5000,123,88,
              '王刚',buyObject,1,1,1,5000,123,200,
              '李云',buyObject,1,1,1,5000,123,100]
for i in range(len(buyRecords)):
	if buyRecords[i] == '毛小':
		buyRecords[i] = '毛大'
j=0
aStudent = int(len(buyRecords)/5)

while j < len(Name):
	# for k in range(aStudent):
	num = buyRecords[8*j+2]*buyRecords[8*j+5]+\
	      buyRecords[8*j+3]*buyRecords[8*j+6]+\
	      buyRecords[8*j+4]*buyRecords[8*j+7]
	everyoneMoney.append(num)
	j+=1

j=0
while j<len(Name):
	print(Name[j],'购买的总金额为%d'%everyoneMoney[j])
	j+=1
j=0
totalMoney = 0
while j < len(Name):
	totalMoney = totalMoney + everyoneMoney[j]
	j+=1
print('总投入的金额为：%d'%totalMoney)



