


n = int(input("请输入一个大于0的整数n，n="))
num=0
weishu = 0
jinwei = 10
for i in range(1,5):
	if n<=(10**i):
		weishu = i
		break
print("weishu",weishu)
for j in range(n):
	if (j+2)%jinwei<=4:
		num=num+1







