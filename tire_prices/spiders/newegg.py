# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tire_prices.items import NeweggItem
import datetime


# from scrapy_splash import SplashRequest

class NeweggSpider(CrawlSpider):
    name = 'newegg'
    allowed_domains = ['newegg.com']
    start_urls = []
    for i in range(1, 25):
        start_urls.append('https://www.newegg.com/p/pl?d=MFP&Page=' + str(i))
    custom_settings = {
        'ITEM_PIPELINES': {'tire_prices.pipelines.NeweggPipeline': 210}
    }
    rules = (
        Rule(LinkExtractor(allow=r'https://www.newegg.com/.*page=\d{1,2}'), follow='True'),
        Rule(LinkExtractor(allow=r'https://www.newegg.com/.*Description=MFP.*-Product'), callback='parse_item'),
    )

    # def parse_item(self, response):
    #     link = response.url
    #     yield SplashRequest(link, self.parse_full, args={'wait': 5})  # SplashRequest進行處理並交個parse_full
    def parse_item(self, response):
        item = NeweggItem()
        response = response.replace(body=response.body.replace(b'<br>', b' ').replace(b'"', b'').replace(b':', b'~'))
        keys = response.xpath('//fieldset/dl/dt[1]//text()').extract()
        values = response.xpath('//fieldset/dl/dd[1]/text()').extract()
        data = dict(zip(keys, values))
        if len(data) >= 10:
            item['date'] = str(datetime.date.today())
            item['shop'] = 'NewEgg'
            item['country'] = 'USA'
            if 'Brand' in data.keys():
                item['brand'] = data['Brand']
            else:
                item['brand'] = 'N/A'
            if 'Series' in data.keys():
                item['series'] = data['Series']
            else:
                item['series'] = 'N/A'
            if 'Model' in data.keys():
                item['model'] = data['Model']
            else:
                item['model'] = 'N/A'
            if 'Part Number' in data.keys():
                item['code'] = data['Part Number']
            else:
                item['code'] = 'N/A'
            if 'Recommended Use' in data.keys():
                item['type'] = data['Recommended Use']
            else:
                item['type'] = 'N/A'
            if 'Functions' in data.keys():
                item['functions'] = data['Functions']
            else:
                item['functions'] = 'N/A'
            if 'Display' in data.keys():
                item['display'] = data['Display']
            else:
                item['display'] = 'N/A'
            if 'Output Type' in data.keys():
                item['output_type'] = data['Output Type']
            else:
                item['output_type'] = 'N/A'
            if 'Laser Technology' in data.keys():
                item['laser_tech'] = data['Laser Technology']
            else:
                item['laser_tech'] = 'N/A'
            if 'Black Print Speed' in data.keys():
                item['black_ppm'] = data['Black Print Speed']
            else:
                item['black_ppm'] = 'N/A'
            if 'Color Print Speed' in data.keys():
                item['color_ppm'] = data['Color Print Speed']
            else:
                item['color_ppm'] = 'N/A'
            if 'Black Print Quality' in data.keys():
                item['black_resolution'] = data['Black Print Quality']
            else:
                item['black_resolution'] = 'N/A'
            if 'Time To First Page (seconds)' in data.keys():
                item['time_to_first_page'] = data['Time To First Page (seconds)']
            else:
                item['time_to_first_page'] = 'N/A'
            if 'Print Languages, std.' in data.keys():
                item['print_language'] = data['Print Languages, std.']
            else:
                item['print_language'] = 'N/A'
            if 'Duplex printing' in data.keys():
                item['duplex_print'] = data['Duplex printing']
            else:
                item['duplex_print'] = 'N/A'
            if 'Max. Duty Cycle' in data.keys():
                item['max_duty_cycle'] = data['Max. Duty Cycle']
            else:
                item['max_duty_cycle'] = 'N/A'
            if 'Copy Speed, Black' in data.keys():
                item['copy_ppm_black'] = data['Copy Speed, Black']
            else:
                item['copy_ppm_black'] = 'N/A'
            if 'Copy Speed, Color' in data.keys():
                item['copy_ppm_color'] = data['Copy Speed, Color']
            else:
                item['copy_ppm_color'] = 'N/A'
            if 'Copy Quality, Black' in data.keys():
                item['copy_resolution_black'] = data['Copy Quality, Black']
            else:
                item['copy_resolution_black'] = 'N/A'
            if 'Max. Document Enlargement' in data.keys():
                item['max_doc_enlargement'] = data['Max. Document Enlargement']
            else:
                item['max_doc_enlargement'] = 'N/A'
            if 'Max. Document Reduction' in data.keys():
                item['max_reduct'] = data['Max. Document Reduction']
            else:
                item['max_reduct'] = 'N/A'
            if 'Max. Number of Copies' in data.keys():
                item['max_num_copy'] = data['Max. Number of Copies']
            else:
                item['max_num_copy'] = 'N/A'
            if 'Copy Features' in data.keys():
                item['copy_feature'] = data['Copy Features']
            else:
                item['copy_feature'] = 'N/A'
            if 'Scan Element' in data.keys():
                item['scan_element'] = data['Scan Element']
            else:
                item['scan_element'] = 'N/A'
            if 'Scan Resolution, Optical' in data.keys():
                item['scan_resolution_optical'] = data['Scan Resolution, Optical']
            else:
                item['scan_resolution_optical'] = 'N/A'
            if 'Scan Resolution, Hardware' in data.keys():
                item['scan_resolution_hardware'] = data['Scan Resolution, Hardware']
            else:
                item['scan_resolution_hardware'] = 'N/A'
            if 'Scan Features' in data.keys():
                item['scan_feature'] = data['Scan Features']
            else:
                item['scan_feature'] = 'N/A'
            if 'Color Fax' in data.keys():
                item['color_fax'] = data['Color Fax']
            else:
                item['color_fax'] = 'N/A'
            if 'Fax Transmission Speed' in data.keys():
                item['fax_trans_speed'] = data['Fax Transmission Speed']
            else:
                item['fax_trans_speed'] = 'N/A'
            if 'Fax Memory' in data.keys():
                item['fax_memory'] = data['Fax Memory']
            else:
                item['fax_memory'] = 'N/A'
            if 'Fax Resolutions' in data.keys():
                item['fax_resolution'] = data['Fax Resolutions']
            else:
                item['fax_resolution'] = 'N/A'
            if 'Paper Trays, std.' in data.keys():
                item['paper_tray_std'] = data['Paper Trays, std.']
            else:
                item['paper_tray_std'] = 'N/A'
            if 'Paper Trays, max.' in data.keys():
                item['paper_tray_max'] = data['Paper Trays, max.']
            else:
                item['paper_tray_max'] = 'N/A'
            if 'Input Capacity, std.' in data.keys():
                item['input_cap_std'] = data['Input Capacity, std.']
            else:
                item['input_cap_std'] = 'N/A'
            if 'Output Capacity, std.' in data.keys():
                item['output_cap_std'] = data['Output Capacity, std.']
            else:
                item['output_cap_std'] = 'N/A'
            if 'Media Type' in data.keys():
                item['media_type'] = data['Media Type']
            else:
                item['media_type'] = 'N/A'
            if 'Media sizes supported' in data.keys():
                item['media_size_support'] = data['Media sizes supported']
            else:
                item['media_size_support'] = 'N/A'
            if 'USB Ports' in data.keys():
                item['usb_port'] = data['USB Ports']
            else:
                item['usb_port'] = 'N/A'
            if 'Network Ports' in data.keys():
                item['network_port'] = data['Network Ports']
            else:
                item['network_port'] = 'N/A'
            if 'Other Ports' in data.keys():
                item['other_port'] = data['Other Ports']
            else:
                item['other_port'] = 'N/A'
            if 'Processor(MHz)' in data.keys():
                item['processor'] = data['Processor(MHz)']
            else:
                item['processor'] = 'N/A'
            if 'Memory, std.' in data.keys():
                item['memory_std'] = data['Memory, std.']
            else:
                item['memory_std'] = 'N/A'
            if 'Memory, max.' in data.keys():
                item['memory_max'] = data['Memory, max.']
            else:
                item['memory_max'] = 'N/A'
            if 'Power Requirements' in data.keys():
                item['power_requirement'] = data['Power Requirements']
            else:
                item['power_requirement'] = 'N/A'
            if 'Power Consumption' in data.keys():
                item['power_consumption'] = data['Power Consumption']
            else:
                item['power_consumption'] = 'N/A'
            if 'Dimensions' in data.keys():
                item['dimension'] = data['Dimensions']
            else:
                item['dimension'] = 'N/A'
            if 'Weight' in data.keys():
                item['weight'] = data['Weight']
            else:
                item['weight'] = 'N/A'
            if 'Package Contents' in data.keys():
                item['package_content'] = data['Package Contents']
            else:
                item['package_content'] = 'N/A'
            if 'Cartridges Compatible' in data.keys():
                item['tonner'] = data['Cartridges Compatible']
            else:
                item['tonner'] = 'N/A'
            if 'Date First Available' in data.keys():
                item['date_first_available'] = data['Date First Available']
            else:
                item['date_first_available'] = 'N/A'
            yield item
        else:
            print('資料不需要，跳過！')
            pass

