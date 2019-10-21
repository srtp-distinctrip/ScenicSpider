# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScenicspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QunarScenicItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 创建时间
    title_e = scrapy.Field()
    # 文章URL
    address = scrapy.Field()
    # MD5定长转换
    open = scrapy.Field()
    # 封面图URL
    ticket = scrapy.Field()
    # 封面如路径
    url = scrapy.Field()


