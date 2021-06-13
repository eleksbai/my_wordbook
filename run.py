import scrapy
from scrapy.crawler import CrawlerProcess

from wordbook.wordbook.spiders.linux_man import LinuxManSpider

process = CrawlerProcess()


process.crawl(LinuxManSpider)
process.start() # the script will block here until the crawling is finished