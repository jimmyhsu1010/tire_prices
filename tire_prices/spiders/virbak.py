# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tire_prices.items import TirePricesItem
import datetime


class VirbakSpider(CrawlSpider):
    name = 'virbak'
    allowed_domains = ['virbacavto.ru']
    start_urls = ['https://www.virbacavto.ru/catalog/shiny_legkovye/?nav=page-1']
    custom_settings = {
        'ITEM_PIPELINES':{
   'tire_prices.pipelines.TirePricesPipeline': 300,
   'tire_prices.pipelines.MySQLPipeline': 200,}
}

    rules = (
        Rule(LinkExtractor(allow=r'https://www.virbacavto.ru/catalog/goods/shiny_legkovye-.*'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'https://www.virbacavto.ru/catalog/shiny_legkovye/.nav=page-\d{0,3}'), follow=True),
    )

    def parse_item(self, response):
        item = TirePricesItem()
        item["date"] = str(datetime.date.today())
        item["company"] = "Virbac"
        item["brand"] = response.xpath("//a[@id='bx_breadcrumb_3']/@title[1]").get()
        item["season"] = response.xpath("//td[contains(text(), 'Сезон')]/following-sibling::td/a/text()").get().strip()
        item["model"] = response.xpath("//td[contains(text(), 'Модель')]/following-sibling::td/a/text()").get().strip()
        width = response.xpath("//td[contains(text(), 'Ширина протектора')]/following-sibling::td/text()").get().strip()
        profile = response.xpath("//td[contains(text(), 'Высота профиля')]/following-sibling::td/a/text()").get().strip()
        item["size"] = width + "/" + profile
        item["diameter"] = "R" + response.xpath("normalize-space(//td[contains(text(), 'Диаметр')]/following-sibling::td/a/text())").get().replace('"','')
        speed = response.xpath(
            "//td[contains(text(), 'скорости')]/following-sibling::td/text()").get().replace("\r","").replace("\t","").replace("\n","").split(" ",1)[0]
        loading = response.xpath(
            "//td[contains(text(), 'нагрузки')]/following-sibling::td/text()").get().replace("\r","").replace("\t","").replace("\n","").split(" ",1)[0]
        item["index"] = loading + speed
        item["price"] = response.xpath(
            "//span[@class='price']/@content[1]").get().strip()
        yield item
