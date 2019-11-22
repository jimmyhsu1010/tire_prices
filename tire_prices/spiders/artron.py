# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tire_prices.items import PrinterItem
import datetime

class ArtronSpider(CrawlSpider):
    name = 'artron'
    allowed_domains = ['artron.ru']
    start_urls = ['https://artron.ru/catalog/ofisnye-printery-i-mfu/?sp_247%5B0%5D=343&sp_247%5B1%5D=344&sp_179%5B0%5D=395&sp_179%5B1%5D=396&sp_12%5B0%5D=6&sp_12%5B1%5D=8&in_stock=on&SHOWALL_1=1']
    custom_settings = {
        'ITEM_PIPELINES': {'tire_prices.pipelines.PrinterPricePipeline': 100}}
    rules = (
        Rule(LinkExtractor(allow=r'https://artron.ru/catalog/ofisnye-printery-i-mfu/?sp_247%5B0%5D=343&sp_247%5B1%5D=344&sp_179%5B0%5D=395&sp_179%5B1%5D=396&sp_12%5B0%5D=6&sp_12%5B1%5D=8&in_stock=on&PAGEN_1=\d{1,2}'), follow=True),
        Rule(LinkExtractor(allow=r'https://artron.ru/catalog/ofisnye-printery-i-mfu/detail/.*.html'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = {}
        response = response.replace(body=response.body.replace(b'<sup>', b'^').replace(b'</sup>', b'').replace(b'\r\n', b'').replace(b'<b>', b'').replace(b'</b>', b''))
        keys = response.xpath('//div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/table[1]//tr/td[not(@colspan) and position()=1]').extract()
        values = response.xpath('//div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/table[1]//tr/td[2]').extract()
        full_name = response.xpath('//div[1]/div[2]/div[1]/h1/text()').get() # 產品名稱
        item_list = full_name.split(' ') # Split full string to list
        item['code'] = response.xpath("normalize-space(//div[@class='tovar_block_pn']/text())").get().split(' ')[1]
        new_keys = []
        for i in keys:
            key = i.replace('<td>', '').replace('</td>', '').replace('<a>', '').replace('</a>', '').replace('<strong', '').replace('</strong>', '').replace('<p>', '').replace('</p>', '').replace('\xa0', '')
            new_keys.append(key)
        new_values = []
        for j in values:
            value = j.replace('<td>', '').replace('</td>', '').replace('\xa0', ' ').replace('<nobr>', '').replace('</nobr>', '').replace('\t\t\t', '').replace('\t', '').replace('<p>', '').replace('</p>', '')
            new_values.append(value)
        data = dict(zip(new_keys, new_values))
        item['shop'] = 'Regard'
        item['country'] = 'Russia'
        item['date'] = str(datetime.date.today())
        item['price'] = response.xpath('normalize-space(//div[@class="item_current_price"]/text())').get().replace('₽', '').replace(' ', '')

        print(data)
        # return item
