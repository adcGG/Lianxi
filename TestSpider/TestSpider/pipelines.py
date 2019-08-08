# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TestspiderPipeline(object):
    # 必须得写，名字不能变
    def process_item(self, item, spider):
        return item
