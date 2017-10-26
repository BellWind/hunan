# -*- coding: utf-8 -*-
import scrapy
# import re
from scrapy.selector import Selector
from hunan.items import xxgkItem
from scrapy import Request

class XxgkSpider(scrapy.Spider):
    name = 'xxgk'
    allowed_domains = ['www.hunan.gov.cn']
    start_urls = ['http://www.hunan.gov.cn/2015xxgk/']

    def parse(self, response):
        sel = Selector(response)

        # content = response.text
        # pattern = re.compile(r'<li><a href=".*?" target="_blank">.*?</a></li>', re.S)
        # items = re.findall(pattern, content)

        for i in ['2', '3', '4', '5']:
            path = '/html/body/div/div/div/div/div[2]/div[2]/div['+i+']/ul/li'
            sites = sel.xpath(path)
            for site in sites:
                tmp ='{0}{1}'.format(response.url,(site.xpath('a/@href').extract()[0]).lstrip('./'))
                print tmp
                yield Request(tmp , callback = self.parseSub)


    def parseSub(self, response):
        sel = Selector(response)

