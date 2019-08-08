import multiprocessing
from datetime import datetime
def do1(j):
	print("第%d进程！"%(j))
if __name__=="__main__":
	print("开始时间：",datetime.now())
	pool = multiprocessing.Pool()
	for i in range(10):                 # 循环提交10个进程
		pool.apply_async(do1(i,))       # 提交自定义函数的进程任务到进程池
	pool.close()
	pool.join()
	print("结束时间：",datetime.now())