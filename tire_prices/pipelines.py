# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import mysql.connector
from mysql.connector import errorcode, connection
from tire_prices import settings
import logging
from scrapy.exceptions import DropItem
import datetime


class TirePricesPipeline(object):
    def open_spider(self, spider):
        self.file = open('virbac_price.csv', 'a')
        self.writer = csv.writer(self.file)
        # self.writer.writerow(
        #     ['Date', 'Company','Brand', 'Season', 'Model', 'Size', 'Diameter', 'Index', 'Price'])

    def process_item(self, item, spider):
        self.writer.writerow((item['date'], item['company'], item['brand'],
                              item['season'], item['model'],
                              item['size'], item['diameter'], item['index'],
                              item['price']))
        return item

    def close_spider(self, spider):
        self.file.close()


# class MySQLPipeline(object):

    # @classmethod
    # def from_crawler(cls, crawler):
    #     cls.MYSQL_DB_NAME = crawler.settings.get("MYSQL_DB_NAME", 'tire_price')
    #     cls.HOST = crawler.settings.get("MYSQL_HOST", 'localhost')
    #     cls.PORT = crawler.settings.get("MYSQL_PORT", 3306)
    #     cls.USER = crawler.settings.get("MYSQL_USER", 'root')
    #     cls.PASSWD = crawler.settings.get("MYSQL_PASSWD", 'o100011007')
    #     return cls()

    # def open_spider(self, spider):
        #self.conn = mysql.connector.connect(database="tire_price", user="root", password="o100011007", )

    # def close_spider(self, spider):
        #self.conn.close()

    # def process_item(self, item, spider):
        # cursor = self.conn.cursor()
        # values = (
        #     item['date'],
        #     item['company'],
        #     item['brand'],
        #     item['season'],
        #     item['model'],
        #     item['size'],
        #     item['diameter'],
        #     item['index'],
        #     item['price'],
        # )
        # sql = 'INSERT INTO price VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # cursor.execute(sql, values)
        # self.conn.commit()
        #
        # return item


class ZapaskaPricesPipeline(object):
    def open_spider(self, spider):
        self.file = open('zapaska.csv', 'a')
        self.writer = csv.writer(self.file)
        # self.writer.writerow(
        #     ['Date', 'Company','Brand', 'Season', 'Model', 'Size', 'Diameter', 'Index', 'Price'])

    def process_item(self, item, spider):
        self.writer.writerow((item['date'], item['company'], item['brand'],
                              item['season'], item['model'],
                              item['size'], item['diameter'], item['index'],
                              item['price']))
        return item

    def close_spider(self, spider):
        self.file.close()


class PrinterPricePipeline(object):
    def open_spider(self, spider):
        # self.filename = 'regard_price_' + str(datetime.date.today().replace('-', '')) + '.csv'
        self.file = open('regard_price.csv', 'a', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(
            ['日期', '商店', '國家', '品牌', '型號', '原廠代碼', '價格', '類型', '列印類型', '技術', '每月列印量', '最大尺寸', '自動雙面列印', '最大解析度',
             '列印速度', '暖機速度', '第一張打印時間', '掃描器類型', '最大掃描尺寸', '掃描解析度', '雙面掃描', '掃描進紙量',
             '彩色掃描速度', '黑白掃描速度', '複印解析度', '複印速度', '首張複印時間', '紙匣容量', '手動進紙匣容量', '碳粉壽命',
             '介面', 'Wifi 列印', '直接列印', 'Web介面', '支援作業系統', '顯示類型', '顯示器尺寸', '產品尺寸', '產品重量'])

    def process_item(self, item, spider):
        self.writer.writerow((item['date'], item['shop'], item['country'], item['brand'], item['model'], item['code'], item['price'], item['type'],
                              item['print_type'], item['print_tech'], item['qt_print_month'], item['max_size'],
                              item['auto_duplex'], item['max_resolution'], item['print_speed'], item['warm_up'],
                              item['first_print'], item['scanner_type'], item['scanner_size'],
                              item['scanner_resolution'],
                              item['scanner_duplex'], item['scanner_capacity'], item['scanner_speed_color'],
                              item['scanner_speed_b_w'], item['copier_resolution'], item['copier_speed'],
                              item['first_copier_time'], item['tray_capacity'], item['manual_tray_capacity'],
                              item['toner_life'],
                              item['interface'], item['wifi_print'], item['direct_print'], item['web_interface'],
                              item['support_os'],
                              item['display_type'], item['display_size'], item['dimension'], item['weight']))
        return item

    def close_spider(self, spider):
        self.file.close()

class YijialePipeline(object):
    def open_spider(self, spider):
        self.file = open('yijiale.csv', 'a', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(
            ['日期', '分店名稱', '地址'])

    def process_item(self, item, spider):
        self.writer.writerow((item['date'], item['name'], item['address']))
        return item

    def close_spider(self, spider):
        self.file.close()

class ConsumablePipeline(object):
    def open_spider(self, spider):
        self.file = open('consumable.csv', 'a', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(
            ['日期', '品牌', '型號', '適用機型', '壽命', '價格'])

    def process_item(self, item, spider):
        self.writer.writerow((item['date'], item['brand'], item['model'], item['machine'], item['life'], item['price']))
        return item

    def close_spider(self, spider):
        self.file.close()

class NeweggPipeline(object):
    def open_spider(self, spider):
        self.file = open('newegg.csv', 'a', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(
            ['Date', 'Shop', 'Country', 'Brand', 'Series', 'Model', 'Part Number', 'Recommended Use', 'Functions',
             'Display',
             'Output type', 'Laser Technology', 'Black Print Speed', 'Color Print Speed', 'Black Print Quality',
             'Time To First Page (seconds)', 'Print Languages, std.', 'Duplex printing', 'Max. Duty Cycle',
             'Copy Speed, Black', 'Copy Speed, Color',
             'Copy Quality, Black',
             'Max. Document Enlargement', 'Max. Document Reduction', 'Max. Number of Copies', 'Copy Features',
             'Scan Element', 'Scan Resolution, Optical',
             'Scan Resolution, Hardware', 'Scan Features', 'Color Fax', 'Fax Transmission Speed', 'Fax Memory',
             'Fax Resolutions', 'Paper Trays, std.',
             'Paper Trays, max.', 'Input Capacity, std.', 'Output Capacity, std.', 'Media Type', 'Media sizes supported', 'USB Ports', 'Network Ports',
             'Other Ports', 'Processor(MHz)', 'Memory, std.', 'Memory, max.', 'Power Requirements',
             'Power Consumption', 'Dimensions',
             'Weight', 'Package Contents', 'Cartridges Compatible', 'Date First Available'])

    def process_item(self, item, spider):
        self.writer.writerow((item['date'], item['shop'], item['country'], item['brand'], item['series'], item['model'], item['code'],
                              item['type'], item['functions'], item['display'], item['output_type'], item['laser_tech'], item['black_ppm'],
                              item['color_ppm'], item['black_resolution'], item['time_to_first_page'], item['print_language'], item['duplex_print'],
                              item['max_duty_cycle'], item['copy_ppm_black'], item['copy_ppm_color'], item['copy_resolution_black'], item['max_doc_enlargement'],
                               item['max_reduct'], item['max_num_copy'], item['copy_feature'], item['scan_element'], item['scan_resolution_optical'], item['scan_resolution_hardware'],
                              item['scan_feature'], item['fax_trans_speed'], item['fax_memory'], item['fax_resolution'], item['paper_tray_std'], item['paper_tray_max'],
                              item['input_cap_std'], item['output_cap_std'], item['media_type'], item['media_size_support'], item['usb_port'], item['network_port'],
                              item['other_port'], item['processor'], item['memory_std'], item['memory_max'], item['power_requirement'], item['power_consumption'],
                              item['dimension'], item['weight'], item['package_content'], item['tonner'], item['date_first_available']))
        return item

    def close_spider(self, spider):
        self.file.close()