# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from scrapy.exceptions import DropItem

class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('items.json', 'wb')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if item['title'] and item['link']:
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line.encode())
            return item
        else:
            raise DropItem("Missing information in %s" % item)
