import math
def sums(*num):                         # 自定义函数，传递元组数字
	'''
	>>> sums(1,2,3,4,5)
	15
	>>> sums('s',2,3,4,5)
	'''
	total=math.trunc(sums(num))        # 对元组元素求和，并取整数
	return total
	#print("累加为：%f"%(total))
if __name__=='__main__':
	import doctest
	doctest.testmod(verbose=False)     # 调用testmod（）模块，读取两个测试，测试上述函数