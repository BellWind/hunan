# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from scrapy import Request
from hunan.items import xxgkItem

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class XxgkSpider(scrapy.Spider):
    name = 'xxgk'
    allowed_domains = ['www.hunan.gov.cn']
    start_urls = ['http://www.hunan.gov.cn/2015xxgk/']

    def parse(self, response):
        sel = Selector(response)
        for i in range(2,6):
            path = '/html/body/div/div/div/div/div[2]/div[2]/div[{0}]/ul/li'.format(i)
            sites = sel.xpath(path)
            for site in sites:
                str = site.xpath('a/@href').extract_first().lstrip('./')
                tmp = '{0}{1}{2}'.format(response.url, str, 'jgxx/jgld/list.html')
                yield Request(tmp , callback = self.parseSub)
                tmp = '{0}{1}{2}'.format(response.url, str, 'jgxx/jgld/list_1.html')
                yield Request(tmp, callback = self.parseSub)

    def parseSub(self, response):
        sel = Selector(response)
        pattern = re.compile('.*?/jgxx/jgld/', re.S)
        s1 = re.findall(pattern, response.url)[0]
        for i in range(2, 22):
            path = '////tr[{0}]/td[3]'.format(i)
            sites = sel.xpath(path)
            for site in sites:
                s2 = site.xpath('a/@href').extract_first().lstrip('./')
                tmp = '{0}{1}'.format(s1, s2)
                yield Request(tmp, callback = self.parseInfo)

    def parseInfo(self, response):
        sel = Selector(response)
        con = sel.xpath('//body/div/div/div/div/div/div[2]/div/ul/li')
        item = xxgkItem()

        item['index'] = self.normalWord(con[0].xpath('text()').extract_first())

        item['org'] = self.normalWord(con[1].xpath('text()').extract_first())

        item['dep'] = self.normalWord(con[2].xpath('text()').extract_first())

        item['name'] = self.normalWord(con[4].xpath('text()').extract_first())

        item['exp'] = self.normalWord(con[5].xpath('text()').extract_first())


        item['pub'] = self.normalWord(con[6].xpath('text()').extract_first())

        con = sel.xpath('//*[@id="div_content"]/div[2]/table/tr')
        item['duty'] = self.normalWord(con[1].xpath('td[2]/text()').extract_first())

        item['work'] = self.normalWord(con[2].xpath('td[2]/text()').extract_first())

        con = sel.xpath('//*[@id="div_content"]/div[2]/table/tr/td[2]')
        item['intro'] = self.normalWord(con[3].xpath('string(.)').extract_first())

        item['resume'] = self.normalWord(con[4].xpath('string(.)').extract_first())

        return item

    def normalWord(self, str):
        if(str != None):
            str = ''.join(str.split())
        return str