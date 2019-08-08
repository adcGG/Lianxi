import threading,random
from time import *
from datetime import datetime,date,time
tickets=[
	['2018-4-7 8:00','北京','沈阳',10,120],
	['2018-4-7 9:00', '上海', '宁波', 5, 100],
	['2018-4-7 12:00', '天津', '北京', 20, 55],
	['2018-4-7 14:00', '广州', '武汉', 0, 200],
	['2018-4-7 16:00', '重庆', '西安', 3, 180],
	['2018-4-7 18:00', '深圳', '上海', 49, 780],
	['2018-4-7 18:00', '武汉', '长沙', 10, 210],
] # 出发时间 出发站 终点站 数量 价格
def buy_ticket(name,nums,date1,start_station):
	i = 0
	sleep(1)
	for get_record in tickets:
		if get_record[0]==date1 and get_record[1] == start_station:
			if get_record[3]>=nums:
				tickets[i][3] = get_record[3]-nums
				print("%s购买%s,%s,%d张票成功！"%(name,date1,start_station,nums))
				return nums
			else:
				print('%s现在存票数量不够，无法购买！'%(name))
				return -1
		i+=1
	print("%s今日无票，无法购买！"%(name))
	return -1

class MThread(threading.Thread):        # 新增继承Thread类的 子类 MThread
	def __init__(self,target,args):     # 定义类的构造函数__init__
		threading.Thread.__init__(self) # 继承父类的__init__
		self.target = target            # 把自定义的函数传递给类变量
		self.args = args                # 自定义函数参数，传递给类变量
	def run(self):                      # 重写run方法
		self.target(*self.args)         # 线程在此，执行自定义函数

if __name__ == '__main__':
	visitor = [
		('张三',3,'2018-4-7 9:00','上海'),
		('李四', 1, '2018-4-7 14:00', '广州'),
		('王五', 2, '2018-4-7 9:00', '上海'),
	]
	class_do_list = []
	print("开始时间：",datetime.now())
	for get_r in visitor:
		get_one = MThread(target=buy_ticket,args=get_r)
		print(get_one)
		class_do_list.append(get_one)
	for i in range(len(class_do_list)):
		class_do_list[i].start()
	for i in range(len(class_do_list)):
		class_do_list[i].join()
	print("结束时间：",datetime.now())
	print("剩余票数：\n")
	for gets in tickets:
		print(gets)


