import requests
from pymongo.mongo_client import MongoClient    # 导入访问MongoDB客户端接口功能
r = requests.get("http://www.baidu.com/")
dis = {"_id":2,"context":r.text}
mongoClient = MongoClient("localhost",27017)
mongoDatabase = mongoClient.site                # 创建或链接site数据库
mongoCollection = mongoDatabase.T_context       # 在site上创建或链接T_context集合
mongoCollection.insert(dis)                     # 插入dis字典变量到集合
import pprint
for get in mongoCollection.find({"_id":2}):
	pprint.pprint(get)
