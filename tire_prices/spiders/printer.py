# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tire_prices.items import PrinterItem
import datetime



class PrinterSpider(CrawlSpider):
    name = 'printer'
    allowed_domains = ['regard.ru']
    start_urls = ['https://www.regard.ru/catalog/filter/?id=MTgwMDA7MTkyNCw1Mjc1LDUzMTEsNTUxMg==&page=1']
    # start_urls = ['https://www.regard.ru/catalog/tovar18282.htm']
    custom_settings = {
        'ITEM_PIPELINES': {'tire_prices.pipelines.PrinterPricePipeline': 100}}

    rules = (
        Rule(LinkExtractor(allow=r'https://www.regard.ru/catalog/filter/\?id=MTgwMDA7MTkyNCw1Mjc1LDUzMTEsNTUxMg==&page=\d{1,2}'), follow='True'),
        Rule(LinkExtractor(allow=r'https://www.regard.ru/catalog/tovar\d*.htm'), callback='parse_item'),
    )

    def parse_item(self, response):
        response = response.replace(body=response.body.replace(b'<br>', b'')) # 將原碼中的<br>標籤去除
        item = PrinterItem()
        keys = response.xpath('//div[3]/div[1]/table[1]//tr/td[not(@colspan) and position()=1]/text()').extract() # Key的位置
        values = response.xpath('//div[3]/div[1]/table[1]//tr/td[not(@colspan) and position()=2]/text()').extract() # Value的位置
        values = map(lambda x:x.replace('\r\n', '').strip(), values) # 去除values裡面所有的\r\n
        model_list = response.xpath('//div[1]/div[1]/h1[1]/text()').get().split(' ')
        if 'Внимание ' in keys and len(values) - len(keys) == 3:
            keys.remove('Внимание ')
            del values[2:4]
            data = dict(zip(keys, values))
        elif 'Внимание ' in keys and len(values) - len(keys) == 1:
            keys.remove('Внимание ')
            data = dict(zip(keys, values))
        else:
            data = dict(zip(keys, values))
        item['shop'] = 'Regard'
        item['country'] = 'Russia'
        item["date"] = str(datetime.date.today())
        if 'Производитель' in data.keys():
            item['brand'] = data['Производитель']
        else:
            item['brand'] = 'N/A'
        if len(model_list) == 3:
            item['model'] = model_list[2]
        elif len(model_list) >= 4 and 'Konica' in model_list:
            item['model'] = ' '.join(model_list[3:])
        elif len(model_list) >= 4 and 'HP' in model_list:
            item['model'] = ' '.join(model_list[2:-1])
        elif len(model_list) >= 4 and 'Canon' in model_list:
            item['model'] = ' '.join(model_list[2:-1])
        else:
            item['model'] = ' '.join(model_list[2:])
        if 'Код производителя' in data.keys():
            item['code'] = data['Код производителя']
        else:
            item['code'] = 'N/A'
        item['price'] = response.xpath('//div[3]/span[2]/span[1]/text()').get().replace(' ', '') + ' руб.'
        if 'Устройство ' in data.keys():
            item['type'] = data['Устройство ']
        else:
            item['type'] = "N/A"
        if 'Тип печати ' in data.keys():
            item['print_type'] = data['Тип печати ']
        else:
            item['print_type'] = 'N/A'
        if 'Технология печати ' in data.keys():
            item['print_tech'] = data['Технология печати ']
        else:
            item['print_tech'] = 'N/A'
        if 'Количество страниц в месяц ' in data.keys():
            item['qt_print_month'] = data['Количество страниц в месяц ']
        else:
            item['qt_print_month'] = 'N/A'
        if 'Максимальный формат ' in data.keys():
            item['max_size'] = data['Максимальный формат ']
        else:
            item['max_size'] = 'N/A'
        if 'Автоматическая двусторонняя печать ' in data.keys():
            item['auto_duplex'] = data['Автоматическая двусторонняя печать ']
        else:
            item['auto_duplex'] = 'N/A'
        if 'Максимальное разрешение для ч/б печати ' in data.keys():
            item['max_resolution'] = data['Максимальное разрешение для ч/б печати ']
        else:
            item['max_resolution'] = 'N/A'
        if 'Скорость печати ' in data.keys():
            item['print_speed'] = data['Скорость печати ']
        else:
            item['print_speed'] = 'N/A'
        if 'Время разогрева ' in data.keys():
            item['warm_up'] = data['Время разогрева ']
        else:
            item['warm_up'] = 'N/A'
        if 'Время выхода первого отпечатка ' in data.keys():
            item['first_print'] = data['Время выхода первого отпечатка ']
        else:
            item['first_print'] = 'N/A'
        if 'Тип сканера ' in data.keys():
            item['scanner_type'] = data['Тип сканера ']
        else:
            item['scanner_type'] = 'N/A'
        if 'Максимальный формат оригинала ' in data.keys():
            item['scanner_size'] = data['Максимальный формат оригинала ']
        else:
            item['scanner_size'] = 'N/A'
        if 'Разрешение сканера ' in data.keys():
            item['scanner_resolution'] = data['Разрешение сканера ']
        else:
            item['scanner_resolution'] = 'N/A'
        if 'Устройство автоподачи оригиналов ' in data.keys():
            item['scanner_duplex'] = data['Устройство автоподачи оригиналов ']
        else:
            item['scanner_duplex'] = 'N/A'
        if 'Емкость устройства автоподачи оригиналов ' in data.keys():
            item['scanner_capacity'] = data['Емкость устройства автоподачи оригиналов ']
        else:
            item['scanner_capacity'] = 'N/A'
        if 'Скорость сканирования (цветн.) ' in data.keys():
            item['scanner_speed_color'] = data['Скорость сканирования (цветн.) ']
        else:
            item['scanner_speed_color'] = 'N/A'
        if 'Скорость сканирования (ч/б) ' in data.keys():
            item['scanner_speed_b_w'] = data['Скорость сканирования (ч/б) ']
        else:
            item['scanner_speed_b_w'] = 'N/A'
        if 'Максимальное разрешение копира (ч/б) ' in data.keys():
            item['copier_resolution'] = data['Максимальное разрешение копира (ч/б) ']
        else:
            item['copier_resolution'] = 'N/A'
        if 'Скорость копирования ' in data.keys():
            item['copier_speed'] = data['Скорость копирования ']
        else:
            item['copier_speed'] = 'N/A'
        if 'Время выхода первой копии ' in data.keys():
            item['first_copier_time'] = data['Время выхода первой копии ']
        else:
            item['first_copier_time'] = 'N/A'
        if 'Подача бумаги ' in data.keys():
            item['tray_capacity'] = data['Подача бумаги ']
        else:
            item['tray_capacity'] = 'N/A'
        if 'Емкость лотка ручной подачи ' in data.keys():
            item['manual_tray_capacity'] = data['Емкость лотка ручной подачи ']
        else:
            item['manual_tray_capacity'] = 'N/A'
        if 'Ресурс ч/б картриджа/тонера ' in data.keys():
            item['toner_life'] = data['Ресурс ч/б картриджа/тонера ']
        else:
            item['toner_life'] = 'N/A'
        if 'Интерфейсы ' in data.keys():
            item['interface'] = data['Интерфейсы ']
        else:
            item['interface'] = 'N/A'
        if 'Поддержка AirPrint ' in data.keys():
            item['wifi_print'] = data['Поддержка AirPrint ']
        else:
            item['wifi_print'] = 'N/A'
        if 'Прямая печать ' in data.keys():
            item['direct_print'] = data['Прямая печать ']
        else:
            item['direct_print'] = 'N/A'
        if 'Веб-интерфейс ' in data.keys():
            item['web_interface'] = data['Веб-интерфейс ']
        else:
            item['web_interface'] = 'N/A'
        if 'Поддержка ОС ' in data.keys():
            item['support_os'] = data['Поддержка ОС ']
        else:
            item['support_os'] = 'N/A'
        if 'ЖК панель (дисплей) ' in data.keys():
            item['display_type'] = data['ЖК панель (дисплей) ']
        else:
            item['display_type'] = 'N/A'
        if 'Диагональ дисплея ' in data.keys():
            item['display_size'] = data['Диагональ дисплея ']
        else:
            item['display_size'] = 'N/A'
        if 'Размеры ' in data.keys():
            item['dimension'] = data['Размеры ']
        elif 'Размеры (ШхВхГ)' in data.keys():
            item['dimension'] = data['Размеры (ШхВхГ)']
        else:
            item['dimension'] = 'N/A'
        if 'Вес' in data.keys():
            item['weight'] = data['Вес']
        else:
            item['weight'] = 'N/A'
        yield item

