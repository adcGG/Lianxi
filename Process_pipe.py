from multiprocessing import Process,Pipe
def do_send(conn_s,j):
	conn_s.send({'发送序号':j,'鲫鱼':[18,10.5],'鲤鱼':[8,6.2]})
	conn_s.close()

if __name__ == '__main__':
	receive_conn,send_conn = Pipe()
	i = 0
	while i<2:         # 发送两条
		i+=1
		pp = Process(target=do_send,args=(send_conn,i,))    # 调用进程对象，创建发送
		pp.start()                                          # 启动进程发送
		print("接收数据%s成功！"%(receive_conn.recv()))     # 接收管道发送数据
		pp.join()
