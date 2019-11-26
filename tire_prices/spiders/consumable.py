# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tire_prices.items import ConsumableItem
import datetime

class ConsumableSpider(CrawlSpider):
    name = 'consumable'
    allowed_domains = ['regard.ru']
    start_urls = ['https://www.regard.ru/catalog/group38000/page1.htm']
    custom_settings = {
        'ITEM_PIPELINES': {'tire_prices.pipelines.ConsumablePipeline': 180}}
    rules = (
        Rule(LinkExtractor(allow=r'https://www.regard.ru/catalog/group38000/page\d{1,2}.htm'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.regard.ru/catalog/tovar\d*.htm'), callback='parse_item'),
    )

    def parse_item(self, response):
        response = response.replace(body=response.body.replace(b'<br>', b''))
        item = ConsumableItem()
        keys = response.xpath('//div[3]/div[1]/table[1]//tr/td[not(@colspan) and position()=1]/text()').extract()  # Key的位置
        values = response.xpath('//div[2]/div[3]/div[1]/table[1]//tr/td[2]/text()').extract()  # Value的位置
        values = map(lambda x: x.replace('\r\n', '').strip(), values)  # 去除values裡面所有的\r\n
        data = dict(zip(keys, values))
        description = response.xpath("//span[@itemprop='description']/text()").get()
        if description is None:
            pass
        else:
            description = description.split(',')
            if 'тонер-картридж' in description:
                item['date'] = str(datetime.date.today())
                item['brand'] = data['Производитель']
                item['model'] = data['Код производителя']
                item['machine'] = description[2].replace(' для ', '')
                item['life'] = description[3]
                item['price'] = response.xpath('//div[3]/span[2]/span[1]/text()').get()
            else:
                pass
            yield item
