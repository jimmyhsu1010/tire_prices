# -*- coding: utf-8 -*-
import scrapy
from tire_prices.items import TirePricesItem

class ZapaskaTestSpider(scrapy.Spider):
    name = 'zapaska_test'
    allowed_domains = ['www.sibzapaska.ru']
    start_urls = ['https://www.sibzapaska.ru/podbor-shin-i-diskov/?filter=Y&f=shini&set_filter=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA']

    # for i in range(9999):
    #     start_urls.append("https://www.sibzapaska.ru/podbor-shin-i-diskov/shini/66" + str(i).zfill(4) + "/")


    def parse(self, response):
        item = TirePricesItem()
        item["brand"] = response.xpath("//div[2]/div[1]/div[1]/h1[1]/text()").get().split(" ")[1]
        item["season"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/text()").get().split(" ", 1)[1]
        item["model"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/text()").get().split(" ")[1]
        item["size"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/text()").get().split(" ")[1]
        item["index"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/span[2]/text()").get().split(" ")[2]
        item["price"] = response.xpath("//span[@id='price']/@price[1]").get()
        print(item)


