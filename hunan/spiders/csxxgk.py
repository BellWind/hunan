# -*- coding: utf-8 -*-
import scrapy


class CsxxgkSpider(scrapy.Spider):
    name = 'csxxgk'
    allowed_domains = ['www.changsha.gov.cn']
    start_urls = ['http://www.changsha.gov.cn/xxgk/szfxxgkml/#chnl227']

    def parse(self, response):
        pass
