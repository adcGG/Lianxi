# -*- coding: utf-8 -*-
import scrapy
# from scrapyFiled.Csdn.Csdn.items import CsdnItem
from Csdn.items import CsdnItem
class CsdnSpider(scrapy.Spider):
    # 爬虫名，运行爬虫时使用
    name = 'csdn'
    # 域
    allowed_domains = ['blog.csdn.net']
    # 起始url
    start_urls = ['https://blog.csdn.net/vivi_in_purple/article/details/81840268']

    def parse(self, response):
        item = CsdnItem()
        # extract() 获得选择器内容文本，['文本内容']
        item["name"] = response.xpath('//h1[@class="title-article"]/text()').extract()[0]
        item["time"] = response.xpath('//span[@class="time"]/text()').extract()[0]
        item["number"] = response.xpath('//span[@class="read-count"]/text()').extract()[0]
        yield item
