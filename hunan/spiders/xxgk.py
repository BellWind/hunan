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
        if(con != None):
            item = xxgkItem()

            item['index'] = con[0].xpath('text()').extract_first()
            if(item['index'] != None): item['index'] = item['index'].strip()

            item['org'] = con[1].xpath('text()').extract_first()
            if (item['org'] != None): item['org'] = item['org'].strip()

            item['dep'] = con[2].xpath('text()').extract_first()
            if (item['dep'] != None): item['dep'] = item['dep'].strip()

            item['name'] = con[4].xpath('text()').extract_first()
            if (item['name'] != None): item['name'] = item['name'].strip()

            item['exp'] = con[5].xpath('text()').extract_first()
            if (item['exp'] != None): item['exp'] = item['exp'].strip()

            item['pub'] = con[6].xpath('text()').extract_first()
            if (item['pub'] != None): item['pub'] = item['pub'].strip()

            con = sel.xpath('//*[@id="div_content"]/div[2]/table/tr')
            item['duty'] = con[1].xpath('td[2]/text()').extract_first()
            if (item['duty'] != None): item['duty'] = item['duty'].strip()

            item['work'] = con[2].xpath('td[2]/text()').extract_first()
            if (item['work'] != None): item['work'] = item['work'].strip()

            con = sel.xpath('//*[@id="div_content"]/div[2]/table/tr/td[2]')
            item['intro'] = con[3].xpath('string(.)').extract_first()
            if (item['intro'] != None): item['intro'] = item['intro'].strip()

            item['resume'] = con[4].xpath('string(.)').extract_first()
            if (item['resume'] != None): item['resume'] = item['resume'].strip()

            return item
