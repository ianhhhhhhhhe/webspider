# -*- coding: utf-8 -*-
import scrapy
from web.items import WebItem
from scrapy.exceptions import NotConfigured

class webSpider(scrapy.Spider):
    name = "web"

    def start_requests(self):
        for url in self.settings.get('PATH').keys():
            yield scrapy.Request(url=url,
                                 cookies = self.settings.get('COOKIES'),
                                 callback=self.parse,)

    def parse(self, response):
        try:
            root = self.settings.get('PATH')[response.url]['ROOT']
            title = self.settings.get('PATH')[response.url]['TITLE']
            link = self.settings.get('PATH')[response.url]['LINK']
        except TypeError:
            raise NotConfigured('PATH should be a dict value')
        except:
            raise NotConfigured('Url or xpath is not configured, please check settings')

        for sel in response.xpath(root):
            item = WebItem()
            item['title'] = sel.xpath(title).extract()
            item['link'] = sel.xpath(link).extract()
            yield item
