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
# 如果项目已经创建，可能需要调整下项目路径， 主要是scapy.cfg的路径
scrapy startproject wordbook

cd wordbook
scrapy genspider -t crawl linux_man man7.org
scrapy genspider -t crawl python_lib python.org

```

# 使用方法

# 抓取目标
## suricata 文档
https://suricata.readthedocs.io/en/latest/
网页下载成本地文件， 用python去解析html文件，提取单词。
python read_html --label suricata suricata-readthedocs-io-en-suricata-6.0.4/suricata-suricata-6.0.4/index.html
