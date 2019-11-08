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
    date = scrapy.Field() # 爬取日期
    # currency = scrapy.Field() # 爬取當日匯率
    brand = scrapy.Field() # 品牌名稱
    model = scrapy.Field() # 型號
    code = scrapy.Field() # 原廠代號
    price = scrapy.Field() # 價格
    type = scrapy.Field() # 類型
    print_type = scrapy.Field() # 列印類型（黑白或彩色）
    print_tech = scrapy.Field() # 列印技術（噴墨或彩色）
    qt_print_month = scrapy.Field()  # 每月打印張數
    max_size = scrapy.Field() # 最大尺寸
    auto_duplex = scrapy.Field() # 自動雙面列印功能
    max_resolution = scrapy.Field() # 最高解析度
    print_speed = scrapy.Field() # 列印速度
    warm_up = scrapy.Field() # 熱機時間
    first_print = scrapy.Field() # 首張列印時間
    scanner_type = scrapy.Field() # 掃描器類型（Sheetfed或Flatbed）
    scanner_size = scrapy.Field() # 最大掃描尺寸
    scanner_resolution = scrapy.Field() # 掃描dpi
    scanner_duplex = scrapy.Field() # 掃描自動雙面
    scanner_capacity = scrapy.Field() # 掃描進紙容量
    scanner_speed_color = scrapy.Field() # 彩色掃描速度
    scanner_speed_b_w = scrapy.Field() # 黑白掃描速度
    copier_resolution = scrapy.Field() # 複印解析度
    copier_speed = scrapy.Field() # 複印速度
    first_copier_time = scrapy.Field() # 首張複印時間
    tray_capacity = scrapy.Field() # 進紙匣容量
    manual_tray_capacity = scrapy.Field() # 手動進紙匣容量
    toner_life = scrapy.Field() # 碳粉盒壽命
    interface = scrapy.Field() # 介面孔
    wifi_print = scrapy.Field() # WiFi列印
    direct_print = scrapy.Field() # 直接列印（透過相機或手機）
    web_interface = scrapy.Field() # 可透過web-interface來修改印表機或MFP設定
    support_os = scrapy.Field()
    display_type = scrapy.Field() # 資訊顯示方式
    display_size = scrapy.Field()
    dimension = scrapy.Field()
    weight = scrapy.Field()




