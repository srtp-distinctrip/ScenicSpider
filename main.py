__author__ = 'dmxjhg'
__date__ = '2019/8/29 17:22'

from scrapy.cmdline import execute

import sys
import os

# os.path.abspath(__file__) 是当前文件路径：F:\Program Files\爬虫项目\new\Spider\main.py
# os.path.dirname(os.path.abspath(__file__)) 是当前文件所在文件夹的路径：F:\Program Files\爬虫项目\new\Spider
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 调用execute可以执行scrapy脚本
execute(["scrapy", "crawl", "scenic"])
