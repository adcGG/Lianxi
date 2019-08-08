# D:\MongoDB\bin>mongod --dbpath D:\data\db
#

#
# C:\WINDOWS\system32>net start MongoDB
# MongoDB Server 服务正在启动 ..
# MongoDB Server 服务已经启动成功。

# ##D:\MongoDB\bin>net stop MongoDB
# ##MongoDB Server 服务正在停止.
# ##MongoDB Server 服务已成功停止。
#

# D:\MongoDB\bin>mongo.exe
# MongoDB shell version v4.0.10
# connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
# Implicit session: session { "id" : UUID("b2bfc492-0bbd-4551-97d8-0e830c7f48eb") }
# MongoDB server version: 4.0.10
# Server has startup warnings:
# 2019-06-30T04:58:43.366-0700 I CONTROL  [initandlisten]
# 2019-06-30T04:58:43.366-0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
# 2019-06-30T04:58:43.366-0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
# 2019-06-30T04:58:43.366-0700 I CONTROL  [initandlisten]
# ---
# Enable MongoDB's free cloud-based monitoring service, which will then receive and display
# metrics about your deployment (disk utilization, CPU, operation statistics, etc).
#
# The monitoring data will be available on a MongoDB website with a unique URL accessible to you
# and anyone you share the URL with. MongoDB may use this information to make product
# improvements and to suggest MongoDB products and deployment options to you.
#
# To enable free monitoring, run the following command: db.enableFreeMonitoring()
# To permanently disable this reminder, run the following command: db.disableFreeMonitoring()


import pymongo                                    #导入数据库驱动模块
from pymongo.mongo_client import MongoClient      #导入MongoDB客户端服务模块
import pymongo.errors #导入出错模块
try:
	mongoClient = MongoClient('localhost',27017) #建立mongodb数据库客户端连接通道
	mongoDatabase = mongoClient.goods            #若没有goods数据库则建立新空库
	print("数据库连接成功")
	mongoCollection  = mongoDatabase.T_fish      #若没有goods数据库则建立新空库，否则建立与goods数据库的连接

	mongoCollection.remove()
	mongoCollection.insert_many([
		{"_id":"1","date1":"2018年3月28日","name":"黑鱼","nums":"10","price":"28.3","Explain":"Tom"},
		{"_id": "2", "date1": "2018年3月29日", "name": "鲤鱼", "nums": "25", "price": "9.8", "Explain": "John"},
		{"_id": "3", "date1": "2018年3月30日", "name": "鲫鱼", "nums": "30", "price": "23.9", "Explain": "Jack"},
	])
	for row in mongoCollection.find():
		print(row)
except pymongo.errors.PyMongoError as e:
	print("操作MongoDB过程出错：e")
