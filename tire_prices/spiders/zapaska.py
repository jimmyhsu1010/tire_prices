# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tire_prices.items import TirePricesItem

class ZapaskaSpider(CrawlSpider):
    name = 'zapaska'
    allowed_domains = ['www.sibzapaska.ru']
    start_urls = ['https://www.sibzapaska.ru/podbor-shin-i-diskov/shini']

    # headers = {
    #     'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    #     'Origin' : 'https://www.sibzapaska.ru',
    #     'Content-Type' : 'application/x-www-form-urlencoded',
    #     'Referer' : 'https://www.sibzapaska.ru/podbor-shin-i-diskov/shini/'
    # }

    rules = [
        Rule(LinkExtractor(allow=(r'.*/podbor-shin-i-diskov/shini/.*')), callback="", follow=True),
        Rule(LinkExtractor(allow=(r'https://www.sibzapaska.ru/podbor-shin-i-diskov/shini/\d+')), callback='parse_item', follow=False),
    ]

    def parse_item(self, response):
        url = response.url
        item = TirePricesItem()
        item["brand"] = response.xpath("//div[2]/div[1]/div[1]/h1[1]/text()").get().split(" ")[1]
        item["season"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/text()").get().split(" ",1)[1]
        item["model"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/text()").get().split(" ")[1]
        item["size"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/text()").get().split(" ")[1]
        item["index"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/span[2]/text()").get().split(" ")[2]
        item["price"] = response.xpath("//span[@id='price']/@price[1]").get()
        print(item)

    # def start_requests(self):
    #     cookie = (
    #         {'name':'_ga', 'value':'GA1.2.88194000.1561634380'},
    #         {'name':'_gat', 'value':'1'},
    #         {'name':'_gid', 'value':'GA1.2.1624859728.1564064744'},
    #         {'name':'_ym_d', 'value':'1561634399'},
    #         {'name':'_ym_isad', 'value':'2'},
    #         {'name':'_ym_uid', 'value': '1561634399552312239'},
    #         {'name':'BX_USER_ID', 'value':'b653785c1d5b2d5229bf7dc7f2dd1c34'},
    #         {'name':'PHPSESSID', 'value':'aeec79802b68e1567af76114ab37156f'},
    #         {'name':'yabs-sid', 'value':'716865771484019462'}
    #     )
    #     cookies = dict()
    #     for cook in cookie:
    #         cookies[cook['name']]=cook['value']
    #
    #     print(cookies)
    #     yield scrapy.Request(url=self.start_urls[0],
    #                          cookies=cookies,
    #                          headers=self.headers,
    #                          callback=self.parse,
    #                          dont_filter=False)
    # #
    # def _build_request(self, rule, link):
    #     r = scrapy.Request(url=link.url, headers=self.headers, callback=self._response_downloaded)
    #     r.meta.update(rule=rule, link_text=link.text)
    #     return r

