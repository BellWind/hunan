# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from scrapy import Request

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class CsxxgkSpider(scrapy.Spider):
    name = 'csxxgk'
    allowed_domains = ['www.changsha.gov.cn']
    start_urls = ['http://www.changsha.gov.cn/xxgk/szfxxgkml/#chnl227']

    def parse(self, response):
        sel = Selector(response)
        path = "/html/body/div[2]/div/div[2]/div/div[3]/div[1]/ul/li[2]/dl[1]/dt/i/"
        str = sel.xpath(path)
        print str