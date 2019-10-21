# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse

from ScenicSpider.items import QunarScenicItem


class ScenicSpider(scrapy.Spider):
    name = 'scenic'
    allowed_domains = ['travel.qunar.com']
    start_urls = ['http://travel.qunar.com/p-cs300085-chengdu-jingdian']

    def parse(self, response):
        """
        1. 获取文章列表页中的文章的url，交给scrapy下载后，进行具体字段的解析
        2. 获取下一页的url，交给scrapy进行下载，下载完成后交给parse
        """
        # 获取文章列表页中的文章的url，交给scrapy下载后，进行具体字段的解析
        scenic_link = response.xpath('//*[@class="titlink"]/@href').extract()
        for url in scenic_link:
            yield Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)
            pass

        # 获取下一页的url，交给scrapy进行下载，下载完成后交给parse
        next_url = response.xpath('//*[@class="b_paging"]/a[last()]/@href').extract_first('end')
        if next_url != 'end':
            next_url = parse.urljoin(response.url, next_url)
            yield Request(url=next_url, callback=self.parse)
        pass


    def parse_detail(self, response):
        # 实例化一个CnblogsArticleItem对象
        scenic_item = QunarScenicItem()
        # 标题中文
        title_xpath = '//*[@id="js_mainleft"]/div[3]/h1/text()'
        title_selector = response.xpath(title_xpath)
        title_list = title_selector.extract()
        title = title_list[0]

        # 标题英文
        title_e_xpath = '//*[@id="js_mainleft"]/div[3]/h1/span/text()'
        title_e_selector = response.xpath(title_e_xpath)
        title_e_list = title_e_selector.extract()
        title_e = title_e_list[0]

        # 地址
        address_xpath = '//*[@class="td_l"]/dl/dd/span/text()'
        address_selector = response.xpath(address_xpath)
        address_list = address_selector.extract()
        address = address_list[0]

        # 开放时间
        open_xpath = '//*[@class="td_r"]/dl/dd/span/p/text()'
        open_selector = response.xpath(open_xpath)
        open_list = open_selector.extract()
        open = open_list[0]

        # 门票
        ticket_xpath = '//*[@id="mp"]/div[2]/p/text()'
        ticket_selector = response.xpath(ticket_xpath)
        ticket_list = ticket_selector.extract()
        ticket = ticket_list[0]

        # 利用解析出的值填充实例化的CnblogsArticleItem对象
        scenic_item["title"] = title
        scenic_item["title_e"] = title_e
        scenic_item["url"] = response.url
        scenic_item["address"] = address
        scenic_item["open"] = open
        scenic_item["ticket"] = ticket

        # 将CnblogsArticleItem实例yield给pipelines.py
        yield scenic_item

        pass

