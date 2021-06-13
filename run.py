import os
import threading
import time
from scrapy.utils.project import get_project_settings
import scrapy
from scrapy.crawler import CrawlerProcess
from generate_txt import generate_txt
from wordbook.spiders.linux_man import LinuxManSpider

# 最大运行时间，12小时
MAX_RUN_TIME = 60

class Manager:
    def __init__(self):
        self.crawler = CrawlerProcess(get_project_settings())
        self.crawler.crawl(LinuxManSpider)
        self.cache_file = 'linux_man.cache'
        print(self.crawler.crawlers)
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
            start_time = time.time()
            while time.time()-start_time < MAX_RUN_TIME:
                time.sleep(1)
            print("ready close")
            self.crawler.stop()
            crawler_thr.join()
            self.txt.queue.put(None)
            txt_thr.join()
            self.txt.data_to_cache(self.cache_file)
        self.txt.to_txt("linux_man")


if __name__ =='__main__':
    manager = Manager()
    manager.run()




