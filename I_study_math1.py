from function.test_function import *
# import sys
# sys.path[0] = 'D:\pythonlearning\lianxi\\function'
# from test_function import *

print(find_factor(8))
say_ok()

test1('JOJO',12,'男')

watermelon('西瓜','甜','圆形','绿色')
print(watermelon2('西瓜',test = '甜',shape = '圆形',color = '绿色'))

attri_L = [21,'甜','圆形','绿色']
get_L = EditFrult('西瓜',attri_L.copy())
print(get_L,attri_L)

a = lambda x,y:x*y
print(a,a(2,4))

print(recursion_sum(4))

# nums_L = [1,2,3,4,8,16,20,30]
nums_L = [1,2]
print(r_dichotomy(nums_L,2,0,len(nums_L)))
