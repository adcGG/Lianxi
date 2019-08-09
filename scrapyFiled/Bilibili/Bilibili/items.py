# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    param = scrapy.Field() # av 之后的数字
    cover = scrapy.Field() # 图片网址
    cover_left_text_1 = scrapy.Field() # 观看人数
    cover_left_text_2 = scrapy.Field() # 评论数量
    title = scrapy.Field()
    # 在args下
    up_name = scrapy.Field()
    rname = scrapy.Field() # 分区
    tname = scrapy.Field() # 频道

