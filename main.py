from twisted.internet import reactor, defer

from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

import logging

from web.spiders.web_spider import webSpider

def main():
    configure_logging(get_project_settings())
    runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(webSpider)
        reactor.stop()

    crawl()
    reactor.run()

if __name__ == '__main__':
    main()
