import time
import sys
from generate_txt import generate_txt
import argparse
from bs4 import BeautifulSoup
import re

# 命令行脚本
parser = argparse.ArgumentParser(description='解析文本文件， 从中提取单词')


def parser_init():
    parser.add_argument("--label", help="标签",)
    parser.add_argument("target", help="目标文件")
    if(len(sys.argv)==1):
        parser.print_help()
        exit()
    pass


def run():
    with open(args.target) as f:
        soup = BeautifulSoup(f, features='lxml')
    for i in  soup.find_all('p'):
        words = re.split('\W', i.text, re.ASCII)
        generate_txt.add_words(words)
    label = args.label
    if label is None:
        label = time.strftime("%Y_%m_%d")
    cache_file = '{}.cache'.format(label)
    generate_txt.set_cache_file(cache_file)
    generate_txt.start(label)


if __name__ == "__main__":
    parser_init()
    args = parser.parse_args()
    run()

