# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy import signals
from scrapy.exporters import JsonItemExporter
from scrapy.exporters import JsonLinesItemExporter
from scrapy.exporters import CsvItemExporter
from scrapy.exporters import XmlItemExporter
from scrapy.exceptions import DropItem

class BasicPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def process_item(self, item, spider):
        if item['title'] and item['link']:
            self.exporter.export_item(item)
            return item
        else:
            raise DropItem("Missing information in %s" % item)

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

class JsonWriterPipeline(BasicPipeline):
    def spider_opened(self, spider):
        file = open('%s_items.json' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = JsonItemExporter(file)
        self.exporter.start_exporting()

class JsonLinesWriterPipeline(BasicPipeline):
    def spider_opened(self, spider):
        file = open('%s_items.jl' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = JsonLinesWriterPipeline(file)
        self.exporter.start_exporting()

class CsvWriterPipeline(BasicPipeline):
    def spider_opened(self, spider):
        file = open('%s_items.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.start_exporting()

class XmlWriterPipeline(BasicPipeline):
    def spider_opened(self, spider):
        file = open('%s_items.xml' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()
