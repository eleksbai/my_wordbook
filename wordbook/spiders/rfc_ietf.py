import os

os.environ['https_proxy'] = "http://127.0.0.1:8118"
os.environ['http_proxy'] = "http://127.0.0.1:8118"

import re

from generate_txt import generate_txt
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class RfcIetfSpider(CrawlSpider):
    name = 'rfc_ietf'
    allowed_domains = ['ietf.org']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )
    def start_requests(self):
        rfc_code = "4250 4251 4252 4253 4254".split()
        return [scrapy.FormRequest("https://www.ietf.org/rfc/rfc{}.txt".format(i.strip()), callback=self.parse_item) for
                i in rfc_code]

    def parse_item(self, response):
        words = []

        text = re.sub(r'[\s,.!?<>:()]+', ' ', response.text)
        words.extend(text.split())

        generate_txt.spider_item(words)
