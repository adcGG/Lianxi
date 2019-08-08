# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 导入setting模块,可使用定义的相关变量
from Daomu import settings
import pymongo
class DaomuPipeline(object):
    def process_item(self, item, spider):
        print("="*50)
        print(item["BookName"])
        print(item["BookTitle"])
        print(item["zhName"])
        print(item["zhNum"])
        print(item["zhLink"])
        print("="*50)
# 修改setting中ITEM_PIPELINES中的内容，使用下面的类进行存入mongo
class DaomuMongoPipeline(object):
    def __init__(self):
        # 从setting中获取变量的值
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        # 创建数据库连接对象，库对象，集合对象
        conn = pymongo.MongoClient(host=host,port=port)
        db = conn.spiderdb
        self.myset = db.daomubiji

    def process_item(self, item, spider):
        # 把item对象转为字典
        bookInfo = dict(item)
        self.myset.insert(bookInfo)
        print("=============存入数据库成功=======================")
        # return item
