# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tire_prices.items import PrinterItem
import datetime


class PrinterSpider(CrawlSpider):
    name = 'printer'
    allowed_domains = ['market.yandex.ru']
    start_urls = ['https://market.yandex.ru/catalog--printery-i-mfu/54546/list?text=многофункциональный%20принтер&hid=138608&srnum=1842&rs=eJwzMjUy5NLn4uVoPM4qwCTBoFpYb23HxcdxYV47qwAjkK_x5yKI_2EXhwCDxFpu1cYGRocARgBV5g0t&glfilter=4914081%3A12110472&glfilter=16826241%3A16826252%2C16826254%2C16826253%2C16826251&onstock=1&local-offers-first=0&page=1']

    custom_settings = {
        'ITEM_PIPELINES': {'tire_prices.pipelines.PrinterPricePipeline': 100}}

    rules = (
        Rule(LinkExtractor(allow=r'https://market.yandex.ru/catalog--printery-i-mfu.*(page=)\d{1,2}'), follow=True),
        Rule(LinkExtractor(allow=r'https://market.yandex.ru/product--(mfu|printer)-.*'), follow=True),
        Rule(LinkExtractor(allow=r'https://market.yandex.ru/product--(mfu|printer)-.*(/spec?).*'), callback='parse_item')
    )

    def parse_item(self, response):
        item = PrinterItem()
        keys = response.xpath('//div[1]/div/dl/dt[1]/span[1]/text()').extract() # Key的位置
        values = response.xpath('//div[1]/div/dl/dd[1]/span[1]/text()').extract() # Value的位置
        data = dict(zip(keys, values))
        print(data)
        # yield item
