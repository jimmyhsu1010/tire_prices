# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TirePricesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    company = scrapy.Field()
    brand = scrapy.Field()
    season = scrapy.Field()
    model = scrapy.Field()
    size = scrapy.Field()
    diameter = scrapy.Field()
    index = scrapy.Field()
    price = scrapy.Field()


