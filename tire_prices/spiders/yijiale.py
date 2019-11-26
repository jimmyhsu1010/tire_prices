# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tire_prices.items import YijialeItem
import datetime

class Yijiale1Spider(CrawlSpider):
    name = 'yijiale1'
    allowed_domains = ['enjoylovestore.com']
    start_urls = ['http://enjoylovestore.com/about/map/p/1.html']
    custom_settings = {'ITEM_PIPELINES': {
        'tire_prices.pipelines.YijialePipeline': 150}
    }
    rules = (
        Rule(LinkExtractor(allow=r'http://enjoylovestore.com/about/map/p/\d{1,2}.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = YijialeItem()
        address = response.xpath('//div[3]/div[3]/div[1]/ul[1]/li/span[1]/text()').extract()
        name = response.xpath('//div[3]/div[3]/div[1]/ul[1]/li/p[1]/text()').extract()
        dictionary = dict(zip(name, address))
        for i in dictionary:
            item['date'] = str(datetime.date.today())
            item['name'] = i
            item['address'] = dictionary[i]
            yield item
