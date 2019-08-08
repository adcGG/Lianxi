# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        # print(type(response),type(response.text))
        # < class 'scrapy.http.response.html.HtmlResponse'> < class 'str' >
        with open('baidu.html','a',encoding='utf-8') as f:
            f.write(response.text)
