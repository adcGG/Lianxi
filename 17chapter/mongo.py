from pymongo.mongo_client import MongoClient
import random
conn = MongoClient('localhost',27017)
db = conn.stu
myset = db.class4
myset1 = db.class0
# # myset.insert({'name':'张铁林','King':'乾隆'})
# myset.insert([{'name':'张国立','King':'康熙'},
#              {'name':'陈道明','King':'康熙'}])
# myset.save({'_id':1,'name':'吴奇隆2','King':'四爷2'})

# cursor = myset.find({},{'_id':0})
# cursor = myset.find_one({},{'_id':0})
# print(cursor)
# for i in cursor:
# 	print(i)

# class0 = db.class0
# # query = {'$or':[{'sex':'w'},{'age':{'$lt':20}}]}
# # cursor = class0.find(query,{'_id':0})
# # # for i in cursor:
# # # 	print(i)
# # # print(cursor.next())
# # # print(cursor.next())
# # for i in cursor:
# # 	print(i)

# myset1.update({'name':'Jame'},{'$set':{'age':22}},multi = True)

#如果文档不存在则插入
# myset.update({'name':'梁家辉'},{'$set':{'King':'咸丰'}},upsert = True)
# myset.update_many({'King':'康熙'},{'$set':{'KingName':'玄烨'}})

# myset.remove({'King':'四爷'})
# myset.remove({'King':'咸丰'},multi = False)
# myset.remove({'KingName':{'$exists':1}})
# myset.find_one_and_delete({'King':'咸丰'})

# #索引操作
class0 = db.class0
#index = 返回一个索引名称
# index = class0.ensure_index('name')
# #创建逆向索引
# index = class0.ensure_index([('age',-1)])
# #获取当前集合中索引
# for i in myset.list_indexes():
# 	print(i)
#删除所有索引
# class0.drop_indexes()
# class0.drop_index(index)#通过名称删除索引
# #创建复合索引
# class0.ensure_index([('name',1),('age',-1)])
# #唯一索引
# class0.ensure_index('_id',name = "MyIndex",unique = True)
# #稀疏索引
# class0.ensure_index('age',sparse = True)
# class4 = db.class4
# p = [{'$group':{'_id':'$King','count':{'$sum':1}}},{'$match':{'count':{'$gt':1}}}]
# cursor =  class4.aggregate(p)
# for i in cursor:
# 	print(i)
# print('为所有人添加score域')
# gradedb = conn.grade
# classtable = gradedb['class']
# cursor = classtable.find({},{'_id':0})
# namespace = []
# for i in cursor:
# 	namespace.append(i['name'])
# print('namespace:',namespace)
# for i in range(len(namespace)):
# 	classtable.update_many({'name':namespace[i]},
# 	                       {'$set':{'chinese':int(random.uniform(60,100)),
# 	                                'math':int(random.uniform(60,100)),
# 	                                'english':int(random.uniform(60,100))}})
#
# print('----------------------')
# cursor = classtable.find({},{'_id':0})
# for i  in cursor:
# 	print(i)
# print('----------------------')
# print('按照性别分组统计每组人数')
# count_for_sex = [{'$group':{'_id':'$sex','count':{'$sum':1}}}]
# cursor = classtable.aggregate(count_for_sex)
# for i in cursor:
# 	print(i)
# print('统计每名男生语文成绩')
# count_boy_chinese = [{'$match':{'sex':'m'}},{'$group':{'_id':'$name','chinesescore':{'$sum':'$chinese'}
#                                 }},]
#
# cursor = classtable.aggregate(count_boy_chinese)
# for  i in cursor:
# 	print(i)
# print('将女生按照英语成绩降序排列')
# gril_sort_reverse_engilsh = [{'$match':{'sex':'w'}},
#                              {'$group':{'_id':'$name','englishscore':{'$sum':'$english'}}},
#                              {'$sort':{'englishscore':-1}}]
# cursor = classtable.aggregate(gril_sort_reverse_engilsh)
# for i in cursor:
# 	print(i)

#grid_write
#将文件以grid方案存放到数据库（D:/a.mp4）
# import gridfs
# import os
# conn2 = MongoClient('localhost',27017)
# griddb = conn2.log
# #获取gridfs对象
# fs = gridfs.GridFS(griddb)
# f = open('D:/a.mp4','rb')
# fs.put(f.read(),filename = 'a.mp4')
# conn2.close()
#
# print("Done")
#

# # grid_read
# # 将文件以grid方案存放到数据库（D:/a.mp4）
# import gridfs
# import os
# conn2 = MongoClient('localhost',27017)
# griddb = conn2.log
# fs = gridfs.GridFS(griddb)
# files = fs.find() # 两个集合共同的生成的对象
# for file in files:
# 	if file.filename == 'a.mp4':
# 		with open(file.filename,'wb') as f:
# 			#从数据库读取内容
# 			data = file.read()
# 			#写入本地
# 			f.write(data)
# conn2.close()
# print('done')

#
# 存储文件
import gridfs
import bson.binary
conn2 = MongoClient('localhost',27017)
griddb = conn2.image
myset2 = griddb.MM
# f = open('D:/a.mp4','rb')
# #将图片内容转换为可存储的二进制格式
# content = bson.binary.Binary(f.read())
# #插入文档
# myset2.insert({'filename':'a.mp4','data':content})

#提取MP4
mp4 = myset2.find_one({'filename':'a.mp4'})
#将内容写入到本地
with open('a.mp4','wb') as f:
	f.write(mp4['data'])

conn2.close()


print('Done')




conn.close()
