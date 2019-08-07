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

class MySQLPipeline(object):

    # @classmethod
    # def from_crawler(cls, crawler):
    #     cls.MYSQL_DB_NAME = crawler.settings.get("MYSQL_DB_NAME", 'tire_price')
    #     cls.HOST = crawler.settings.get("MYSQL_HOST", 'localhost')
    #     cls.PORT = crawler.settings.get("MYSQL_PORT", 3306)
    #     cls.USER = crawler.settings.get("MYSQL_USER", 'root')
    #     cls.PASSWD = crawler.settings.get("MYSQL_PASSWD", 'o100011007')
    #     return cls()

    def open_spider(self, spider):
        self.conn = mysql.connector.connect(database="tire_price", user="root", password="o100011007",)


    def close_spider(self, spider):
        self.conn.close()


    def process_item(self, item, spider):
        cursor = self.conn.cursor()
        values = (
            item['date'],
            item['company'],
            item['brand'],
            item['season'],
            item['model'],
            item['size'],
            item['diameter'],
            item['index'],
            item['price'],
        )
        sql = 'INSERT INTO price VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, values)
        self.conn.commit()

        return item

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

