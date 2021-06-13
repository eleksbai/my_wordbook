import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from generate_txt import generate_txt


class PythonLibSpider(CrawlSpider):
    name = 'python_lib'
    allowed_domains = ['python.org']
    start_urls = ['https://docs.python.org/3/library/index.html']

    rules = (
        Rule(LinkExtractor(allow=r'3/library/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        words = []
        for i in response.xpath('//p/text()').getall():
            text = re.sub(r'[\s,.!?<>:()]+', ' ', i.lower())
            words.extend(text.split())
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        generate_txt.spider_item(words)
