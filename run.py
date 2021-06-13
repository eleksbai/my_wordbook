import os
import threading
import time
from scrapy.utils.project import get_project_settings
import scrapy
from scrapy.crawler import CrawlerProcess
from generate_txt import generate_txt
from wordbook.spiders.linux_man import LinuxManSpider
from wordbook.spiders.python_lib import PythonLibSpider

# 最大运行时间，12小时
MAX_RUN_TIME = 60*60*12

class Manager:
    def __init__(self):
        self.crawler = CrawlerProcess(get_project_settings())
        self.crawler.crawl(PythonLibSpider)
        self.cache_file = 'python_lib.cache'
        self.txt = generate_txt


    def crawler_worker(self):
        self.crawler.start()
        self.crawler.stop()

    def run(self):
        if  os.path.exists(self.cache_file):
            self.txt.cache_to_data(self.cache_file)
        else:
            txt_thr = threading.Thread(target=self.txt.loop)
            txt_thr.start()
            crawler_thr = threading.Thread(target=self.crawler_worker)
            crawler_thr.start()
            crawler_thr.join(timeout=MAX_RUN_TIME)
            print("ready close")
            self.crawler.stop()

            self.txt.queue.put(None)
            txt_thr.join()
            self.txt.data_to_cache(self.cache_file)
        self.txt.to_txt("python_lib")


if __name__ =='__main__':
    manager = Manager()
    manager.run()




