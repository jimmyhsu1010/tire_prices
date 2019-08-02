# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tire_prices.items import TirePricesItem
from scrapy.http import FormRequest

class ZapaskaSpider(scrapy.Spider):
    name = 'zapaska'
    allowed_domains = ['www.sibzapaska.ru']
    # start_urls = ["https://www.sibzapaska.ru/podbor-shin-i-diskov/?ajax=y&=17&filter=Y&f=shini&arrFilter_P3_MIN=1&arrFilter_P3_MAX=31590.00"]
    custom_settings = {}

    headers = {
        'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Origin' : 'https://www.sibzapaska.ru',
        'x-requested-with': 'XMLHttpRequest',
        # 'Referer' : 'https://www.sibzapaska.ru/podbor-shin-i-diskov/shini/'
    }

    def start_requests(self):
        url = "https://www.sibzapaska.ru/include/ajax/shini.php"
        requests = []
        for i in range(1,10):
            formdata = {
                "iblock" : "17",
                "PAGEN_1" : str(i),
                "kol" : "24",
                "by1" : "CATALOG_PRICE_1",
                "or1" : "ASC",
                "by2" : "SHOW_COUNTER",
                "or2" : "DESC",
                "min" : "1",
                "max" : "31590.00"
            }
            request =  FormRequest(url, callback=self.parse, formdata=formdata, headers=self.headers, method="POST")
            requests.append(request)
        return requests

    def parse(self, response):
        ref = "https://www.sibzapaska.ru"
        contents = response.xpath("//a[@class='item__name']/@href").extract()
        for url in contents:
            link = ref + url
            # print(link)
            yield scrapy.Request(url=link, callback=self.parse_item, dont_filter=True)



    def parse_item(self, response):
        url = response.url
        # item = TirePricesItem()
        # item["brand"] = response.xpath("//div[2]/div[1]/div[1]/h1[1]/text()").get().split(" ")[1]
        # item["season"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/text()").get().split(" ",1)[1]
        # item["model"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/text()").get().split(" ")[1]
        # item["size"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/text()").get().split(" ")[1]
        # item["index"] = response.xpath("//div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/span[2]/text()").get().split(" ")[2]
        # item["price"] = response.xpath("//span[@id='price']/@price[1]").get()
        print(response)


