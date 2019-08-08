from Class_module import *
import os

def save_file(file_name,L_newRecord):
	flag = False
	if type(L_newRecord)!=list:
		print('保存内容必须以列表对象格式进行！保存失败！')
		return flag
	cur_path = os.path.abspath(os.path.curdir)
	cur_path = cur_path+'\\'+file_name
	try:
		f1 = open(cur_path,'w')
		f1.writelines(L_newRecord)
		flag = True
	except:
		flag = False
	finally:
		if flag:
			f1.close()
	return flag
#==================================创建大礼盒实例,并求相关值
L_SaveData = []
big_gift_box = FishBox(60,30,40)
big_gift_box.price = 1000
big_gift_box.amount = 20
big_gift_box.weigth = 10
L_SaveData.append("大礼盒的体积是"+str(big_gift_box.volume())+'立方厘米\n')
L_SaveData.append('大礼盒的表面积是'+str(big_gift_box.area())+'平方厘米\n')
index = big_gift_box.type.index('大礼盒')
g_box_num = big_gift_box.countBoxNums(200,index)
L_SaveData.append('200条鱼需要'+str(g_box_num)+'只大礼盒\n')
L_SaveData.append('200条鱼装大礼盒的价值为'+str(g_box_num*big_gift_box.price)+'元\n')

#==================================创建小礼盒实例,并求相关值
small_gift_box = FishBox(50,20,30)
small_gift_box.price = 500
small_gift_box.amount = 10
small_gift_box.weigth = 5
L_SaveData.append("小礼盒的体积是"+str(small_gift_box.volume())+'立方厘米\n')
L_SaveData.append('小礼盒的表面积是'+str(small_gift_box.area())+'平方厘米\n')
index = small_gift_box.type.index('小礼盒')
g_box_num = small_gift_box.countBoxNums(200,index)
L_SaveData.append('200条鱼需要'+str(g_box_num)+'只小礼盒\n')
L_SaveData.append('200条鱼装小礼盒的价值为'+str(g_box_num*small_gift_box.price)+'元\n')

if save_file('fish_records.txt',L_SaveData):
	print('三酷猫装盒子数据保存成功！')
else:
	print('三酷猫装盒子保存失败！')


