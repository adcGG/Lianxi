import pymongo
from pymongo.mongo_client import MongoClient
import pymongo.errors
try:
	mongoClient = MongoClient("127.0.0.1",27017)
	mongoDatabase = mongoClient.goods

	print("数据库连接成功")
	mongoCollection = mongoDatabase.T_fish

	mongoCollection.update({"_id":"1"},{"$set":{'nums':'20'}})
	mongoCollection.delete_one({'_id':'3'})
	for row in mongoCollection.find():
		print(row)
except pymongo.errors.PyMongoError as e:
	print("mongo Error:",e)