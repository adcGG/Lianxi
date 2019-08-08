# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from Csdn import settings
import pymongo

class CsdnPipeline(object):
    def process_item(self, item, spider):
        print(item["name"])
        print(item["time"])
        print(item["number"])

class CsdnMongoPipeline(object):
    def __init__(self):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        conn = pymongo.MongoClient(host=host,port=port)
        db = conn.spiderdb
        self.myset = db.csdn
    def process_item(self, item, spider):
        Info = dict(item)
        self.myset.insert(Info)
        print("="*40,'存入数据库成功','='*40)



