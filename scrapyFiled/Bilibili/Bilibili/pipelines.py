# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy,pymysql
from Bilibili import settings

class BilibiliPipeline(object):
    def __init__(self):
        host = settings.MYSQL_HOST
        user = settings.MYSQL_USER
        pwd = settings.MYSQL_PWD
        dbName = settings.MYSQL_DB
        self.db = pymysql.connect(host = host,user=user,password = pwd
                                  ,db=dbName,charset="utf8")
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        sql = "insert into bilibili (param,cover,cover_left_text_1,cover_left_text_2," \
              "title,up_name,rname,tname) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        List = ['av'+item["param"],item["cover"],item["cover_left_text_1"],item["cover_left_text_2"],
                item["title"],item["up_name"],item["rname"],item["tname"]]
        self.cursor.execute(sql,List)
        self.db.commit()
        print("="*80)
        print("存入数据库成功")
        print("="*80)

class BilibiliImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print("x"*40)
        print(item)
        print(type(item))
        image_Link = item["cover"]
        yield scrapy.Request(image_Link)