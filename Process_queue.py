from multiprocessing import Process,Queue
q_object = Queue(5)         # 创建5个元素的队列实例
def SendData(qObject,data):
	qObject.put(data)       # 发送函数，通过队列对象，qObject发送data

def receiveData(qObject):
	if qObject.empty()>0:
		print("队列信息为空!")
	else:
		show_data = qObject.get()
		print("输出%s"%(show_data))

if __name__=='__main__':
	send_data = [0,'Tom',10,'China']
	for i in range(5):
		send_data[0]=i      # 对列表第一个元素值进行修改
		p1 = Process(target=SendData,args=(q_object,send_data))
		p1.start()
		p2 = Process(target=receiveData,args=(q_object,))
		p2.start()


