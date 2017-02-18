# -*- coding: utf-8 -*-
import scrapy
from web.items import WebItem

class webSpider(scrapy.Spider):
    name = "web"

    def start_requests(self):
        for url in self.settings.get('PATH').keys():
            yield scrapy.Request(url=url,
                                 cookies = self.settings.get('COOKIES'),
                                 callback=self.parse,)

    def parse(self, response):
        for sel in response.xpath(self.settings.get('PATH')[response.url]['ROOT']):
            item = WebItem()
            item['title'] = sel.xpath(self.settings.get('PATH')[response.url]['TITLE']).extract()
            item['link'] = sel.xpath(self.settings.get('PATH')[response.url]['LINK']).extract()
            yield item
