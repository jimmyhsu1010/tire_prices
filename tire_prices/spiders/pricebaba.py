# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tire_prices.items import PrinterItem
import datetime

class PricebabaSpider(CrawlSpider):
    name = 'pricebaba'
    allowed_domains = ['pricebaba.com']
    start_urls = ['https://pricebaba.com/search?PRINTERS-GEN-PRIMET=OPT-1463478167314&category=PRINTERS&from=Printers&start=0&sort=popularity-desc&status=10&status=20&status=30&status=40&limit=40&active=true&page=1']
    custom_settings = {
        'ITEM_PIPELINES': {'tire_prices.pipelines.PrinterPricePipeline': 100}}
    rules = (
        Rule(LinkExtractor(allow=r'https://pricebaba.com/.*page=\d{1,2}'), follow=True),
        Rule(LinkExtractor(allow=r'https://pricebaba.com/printers/.*'), callback='parse_item'),
    )

    def parse_item(self, response):
        response = response.replace(body=response.body.replace(b'<sup>', b'^').replace(b'</sup>', b'').replace(b'\r\n', b'').replace(b'<b>', b'').replace(b'</b>', b''))
        item = PrinterItem()
        item['date'] = str(datetime.date.today())
        item['shop'] = 'Pricebaba'
        item['country'] = 'India'
        item['brand'] = response.xpath('//div[6]/div[1]/ul[1]/li[3]/a[1]/text()').get()
        del_list = ['Multi', 'Function', 'Laser', 'Printer', 'Price', 'Single']
        full_name = response.xpath('normalize-space(//div[6]/div[1]/ul[1]/li[4]/text())').get().split(' ')
        item['brand'] = response.xpath('//div[6]/div[1]/ul[1]/li[3]/a[1]/text()').get()
        brand_list = response.xpath('//div[6]/div[1]/ul[1]/li[3]/a[1]/text()').get().split(' ')
        for brand in brand_list:
            if brand in full_name:
                full_name.remove(brand)
        for i in del_list:
            if i in full_name:
                full_name.remove(i)
                model = ' '.join(full_name)
        item['model'] = model
        item['code'] = model
        if len(response.xpath('normalize-space(//li[1]/div[1]/div[1]/div[2]/span[1]/text())').get().replace(',', '').replace('Rs. ', '')) != 0:
            item['price'] = float(response.xpath('normalize-space(//li[1]/div[1]/div[1]/div[2]/span[1]/text())').get().replace(',', '').replace('Rs. ', ''))
        else:
            item['price'] = 'N/A'
        keys = response.xpath('//table[1]/tbody[1]/tr/td[1]/text()').extract()
        values = response.xpath('//table[1]/tbody[1]/tr/td[2]/text()').extract()
        data = dict(zip(keys, values))
        item['type'] = data['Functions']
        if 'Print Output' in data.keys():
            item['print_type'] = data['Print Output']
        else:
            item['print_type'] = 'N/A'
        if 'Printing Method' in data.keys():
            item['print_tech'] = data['Printing Method']
        else:
            item['print_tech'] = 'N/A'
        if 'Duty Cycle' in data.keys():
            item['qt_print_month'] = data['Duty Cycle']
        else:
            item['qt_print_month'] = 'N/A'
        if 'Media Size Supported' in data.keys():
            item['max_size'] = data['Media Size Supported']
        else:
            item['max_size'] = 'N/A'
        if 'Duplex Print' in data.keys():
            item['auto_duplex'] = data['Duplex Print']
        else:
            item['auto_duplex'] = 'N/A'
        if 'Max Print Resolution (Mono)' in data.keys():
            item['max_resolution'] = data['Max Print Resolution (Mono)']
        else:
            item['max_resolution'] = 'N/A'
        if 'Print Speed Mono' in data.keys():
            item['print_speed'] = data['Print Speed Mono']
        else:
            item['print_speed'] = 'N/A'
        item['warm_up'] = 'N/A'
        if 'First Print Out Time (Mono)' in data.keys():
            item['first_print'] = data['First Print Out Time (Mono)']
        else:
            item['first_print'] = 'N/A'
        if 'Scan Type' in data.keys():
            item['scanner_type'] = data['Scan Type']
        else:
            item['scanner_type'] = 'N/A'
        item['scanner_size'] = 'N/A'
        if 'Optical Scanning Resolution' in data.keys():
            item['scanner_resolution'] = data['Optical Scanning Resolution']
        else:
            item['scanner_resolution'] = 'N/A'
        item['scanner_duplex'] = 'N/A'
        if 'Auto Document Feeder' in data.keys():
            item['scanner_capacity'] = data['Auto Document Feeder']
        else:
            item['scanner_capacity'] = 'N/A'
        item['scanner_speed_color'] = 'N/A'
        item['scanner_speed_b_w'] = 'N/A'
        if 'Copy Resolution Mono' in data.keys():
            item['copier_resolution'] = data['Copy Resolution Mono']
        else:
            item['copier_resolution'] = 'N/A'
        if 'Copy Speed Mono' in data.keys():
            item['copier_speed'] = data['Copy Speed Mono']
        else:
            item['copier_speed'] = 'N/A'
        if 'First Copy Out Time' in data.keys():
            item['first_copier_time'] = data['First Copy Out Time']
        else:
            item['first_copier_time'] = 'N/A'
        if 'Input Tray Capacity' in data.keys():
            item['tray_capacity'] = data['Input Tray Capacity']
        else:
            item['tray_capacity'] = 'N/A'
        item['manual_tray_capacity'] = 'N/A'
        item['toner_life'] = 'N/A'
        if 'Ethernet Support' in data.keys() and 'USB support' not in data.keys():
            item['interface'] = data['Ethernet Support']
        elif 'Ethernet Support' and 'USB support' in data.keys():
            item['interface'] = data['Ethernet Support'] + ', USB Support = ' + data['USB support']
        else:
            item['interface'] = 'N/A'
        if 'Wireless Support' in data.keys():
            item['wifi_print'] = data['Wireless Support']
        else:
            item['wifi_print'] = 'N/A'
        item['direct_print'] = 'N/A'
        item['web_interface'] = 'N/A'
        item['support_os'] = 'N/A'
        if 'Display' in data.keys():
            item['display_type'] = data['Display']
        else:
            item['display_type'] = 'N/A'
        item['display_size'] = 'N/A'
        if 'Width' and 'Depth' and 'Height' in data.keys():
            item['dimension'] = data['Width'] + 'x' + data['Depth'] + 'x' + data['Height']
        else:
            item['dimension'] = 'N/A'
        if 'Weight' in data.keys():
            item['weight'] = data['Weight']
        else:
            item['weight'] = 'N/A'
        yield item
