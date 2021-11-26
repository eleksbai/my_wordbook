import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from generate_txt import generate_txt



class LinuxManSpider(CrawlSpider):
    name = 'linux_man'
    allowed_domains = ['man7.org']
    start_urls = ['https://man7.org/linux/man-pages/index.html']

    rules = (
        Rule(LinkExtractor(allow=r'man-pages'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        words = []
        for i in  response.xpath('//pre/text()').getall():
            text = re.sub(r'[\s,.!?<>:()]+', ' ', i.lower())
            words.extend(text.split())
        # 调试异常数据
        # if len(words)>10000:
        #     l_data = sorted([(words.count(i), i) for i in set(words)], reverse=True)
        #     with open('/home/hyman/case/my_wordbook/dist/{}.txt'.format(response.url.split('/')[-1]), 'w') as f:
        #         f.write(response.text)
        #     print("url:", response.url, len(l_data), *l_data[:10])
        generate_txt.add_words(words)
