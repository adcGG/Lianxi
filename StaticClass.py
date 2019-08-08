class StaticC():
	name = 'Tom'
	age = 20
	address = 'China'
	call = 283800
	def a():
		i = 0
		i+=1
		print('第一个函数%d'%(i))

	def b(add = 1):
		print('第二个函数%d'%(add))

	def c(add = 1):
		print('第三个函数%d'%(add))
		return add

s1 = StaticC()
# s1.a()
# Traceback (most recent call last):
#   File "D:\pythonlearning\lianxi\StaticClass.py", line 19, in <module>
#     s1.a()
# TypeError: a() takes 0 positional arguments but 1 was given

print('address:%s,call:%s'%(StaticC.address,StaticC.call))
print(StaticC.a())
print(StaticC.b(2))
print(StaticC.c(3))