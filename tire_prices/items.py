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

class PrinterItem(scrapy.Item):
    date = scrapy.Field()
    brand = scrapy.Field()
    type = scrapy.Field()
    print_type = scrapy.Field()
    print_tech = scrapy.Field()
    qt_print_month = scrapy.Field()
    max_size = scrapy.Field()
    auto_duplex = scrapy.Field()
    max_resolution = scrapy.Field()
    print_speed = scrapy.Field()
    warm_up = scrapy.Field()
    first_print = scrapy.Field()
    scanner_type = scrapy.Field()



