def find_factor(nums):
	'''
	find_factor 是自定义的函数
	:param nums: 传递一个正整数的参数
	:return: 一个正整数的所有因数
	'''
	if type(nums)!=int:
		print('输入值类型出错，必须是正整数')
		return
	if nums <=0:
		print('输入值范围出错，必须是正整数')
		return
	i = 1
	str1 = ''
	while i< nums:
		if nums%i == 0:
			str1 = str1+str(i)+' '
		i+=1
	return str1

def say_ok():
	print('OK')

def test1(name,age,sex):
	print('姓名：%s，年龄：%s，性别：%s'%(name,str(age),sex))

def watermelon(name,*attributes): # 带*的可以传递任意数量值得参数
	print(name)
	print(type(attributes))
	description = ''
	for get_t in attributes:
		description+=' '+get_t
	print(description)
	# 运行结果
	# 西瓜
	# <class 'tuple'>
	# 甜 圆形 绿色


def watermelon2(name,**attributes): # 带**的可以传递任意数量的键值对
	print(name)
	print(type(attributes))
	return attributes

# 运行结果
# 西瓜
# <class 'dict'>
# {'test': '甜', 'shape': '圆形', 'color': '绿色'}

# 列表 和 字典 在传递参数的时候是传递地址的 所以函数内部修改列表（字典）会导致函数外部传递前的变量元素
def EditFrult(name,attributes):
	attributes[0] = attributes[0]*0.9
	return attributes

def recursion_sum(num):
	if num == 1:
		return num
	tt = num+recursion_sum(num-1)
	print('第%d次递归'%(num))
	print('返回值%d在内存中的地址: %d'%(tt,id(tt)))
	return tt

def r_dichotomy(nums,find,left,right):
	middle = (right+left)//2
	print(left,right,middle)
	if nums[middle] == find:
		return middle
	if right == left+1:
		if nums[middle]!=find:
			return -1
	if nums[middle]>find:
		return r_dichotomy(nums,find,left,middle)
	elif nums[middle]<find:
		return r_dichotomy(nums,find,middle+1,right)


