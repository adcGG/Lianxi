class Box1():
	'''
	求立方体 的类
	'''
	def __init__(self,length1,width1,height1,c1 = 0):
		self.length = length1
		self.width = width1
		self.height = height1

	def volume(self):
		return self.length*self.width*self.height

class Box2(Box1):
	def __init__(self,length1,width1,height1):
		super().__init__(length1,width1,height1)
		self.color = 'white'
		self.material = 'paper'
		self.type = 'fish'
	def area(self):
		re = self.length*self.width+self.length*self.height+self.width*self.height
		return re*2

my_box2 = Box2(10,10,10)
print('立方体体积是：%d'%(my_box2.volume()))
print('立方体表面积是%d'%(my_box2.area()))
print('Box 颜色 %s 材质 %s 类型 %s'%(my_box2.color,my_box2.material,my_box2.type))
