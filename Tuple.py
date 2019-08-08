#Tuple 是不可变的序列，也是一种可以存储 各种数据类型 集合，用小括号表示元组的开始和结束，元素之间用逗号分隔
#这里不可变，包括不能对 元组对象进行增加元素、变换元素位置、修改元素、删除元素等操作。元组中每个元素提供对应的一个下标，从0开始
test = (1,2,2,'1','a')
test3 = ('OK',)#为了避免当成数学公式的括号 ，加个逗号 消除歧义
nameAge = 'tom',19
name,Age = 'Alice',20
print(nameAge,type(nameAge))
print(name,Age,'type(name)',type(name),'type(Age)',type(Age))
print(test[:3])
for get_num in test:
	if get_num == '1':
		print("'1'的下标是%d"%test.index('1'))
		break
print('test中 2的数量',test.count(2))
test2 = (1,2,3)
print('用sum计算元组的和(为数字)',sum(test2))
test4 = test+test3
print('test4:',test4)