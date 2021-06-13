# my_wordbook
收集各类感兴趣的单词，通过不背单词的自主上传功能进行背诵记忆。
[自定义词书链接](https://bbdc.cn/lexis_book_index)

# linux-man单词本
分类： 编程
目标： https://man7.org/linux/man-pages/
采集方法： scrapy
说明： linux man 网站包含了大量的技术文档。提取文档中的英文单词进行背诵，当后面需要看文档的时候可以起到事半功倍的效果


# scapy 
[scrapy教程](https://docs.scrapy.org/en/latest/intro/tutorial.html)
```shell
scrapy startproject wordbook
cd wordbook
scrapy genspider -t crawl linux_man man7.org
```


