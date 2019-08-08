class Box1():
	'''
	求立方体 的类
	'''
	def __init__(self,length1,width1,height1,c1 = 0):
		self.length = length1
		self.width = width1
		self.height = height1
		self.color0 = Color(c1).setColor()

	def volume(self):
		return self.length*self.width*self.height

class Color():
	def __init__(self,index = 0):
		self.set_color = ['white','red','black','green']
		self.index = index

	def setColor(self):
		print('index',self.index)
		return self.set_color[self.index]

my_box = Box1(10,10,10,1)
length = my_box.length
print('立方体的体积是：%d'%(my_box.volume()),'长度',length)
