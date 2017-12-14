# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from scrapy import Request
import urllib2
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from hunan.items import csItem

class CsxxgkSpider(scrapy.Spider):
    name = 'csxxgk'
    allowed_domains = ['www.changsha.gov.cn']
    start_urls = ['http://www.changsha.gov.cn/xxgk/szfxxgkml/#chnl227']

    def parse(self, response):
        sel = Selector(response)
        head = "http://www.changsha.gov.cn/xxgk/"

        sites = sel.xpath('//*[@class="deptpubItem"]/a[1]/@href').extract()
        for site in sites:
            if site == None:
                continue
            url = head + site.lstrip('../')
            yield Request(url, callback=self.parse2)

    def parse2(self, response):
        sel = Selector(response)
        tmp = sel.xpath('//*[@id="deptFileList"]/li[1]/ul/li[1]/a/@href').extract_first()
        if tmp == None:
            return
        url = response.url + tmp.lstrip('./')
        yield Request(url, callback=self.parse3)

    def parse3(self, response):
        sel = Selector(response)
        path = '//*[@class="docTitle_link"]/@href'
        urls = sel.xpath(path).extract()

        for url in urls:
            if url == None:
                continue
            url = response.url + url.lstrip('./')
            yield Request(url, callback=self.parse4)

    def parse4(self, response):

        try:
            sel = Selector(response)

            # item = csItem()
            # item['index'] = self.normalWord(sel.xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/ul/li[1]/text()').extract_first())
            index = self.normalWord(
                sel.xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/ul/li[1]/text()').extract_first())
            # item['org'] = self.normalWord(sel.xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/ul/li[2]/text()').extract_first())
            # item['dep'] = self.normalWord(sel.xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/ul/li[3]/text()').extract_first())
            # item['exp'] = self.normalWord(sel.xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/ul/li[6]/text()').extract_first())
            # item['pub'] = self.normalWord(sel.xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/ul/li[7]/text()').extract_first())
            # item['name'] = self.normalWord(sel.xpath('//*[@id="docContent_detail"]//tr[1]/td[3]/text()').extract_first())
            name = self.normalWord(
                sel.xpath('//*[@id="docContent_detail"]//tr[1]/td[3]/text()').extract_first())
            # item['duty'] = self.normalWord(sel.xpath('//*[@id="docContent_detail"]//tr[2]/td[2]/text()').extract_first())
            # item['work'] = self.normalWord(sel.xpath('//*[@id="docContent_detail"]//tr[3]/td[2]/text()').extract_first())
            #
            # tmp = sel.xpath('//*[@id="docContent_detail"]//tr[4]/td[2]')
            # item['resume'] = self.normalWord(tmp.xpath('string(.)').extract_first())
            #
            # print item['name']

            # 下载图片
            path = '//img/@src'
            pattern = re.compile('http://www.changsha.gov.cn/xxgk/.*/', re.S)
            head = re.findall(pattern, response.url)[0]
            tmp = sel.xpath(path).extract_first()
            if tmp == None:
                # return item
                return
            tail = tmp.lstrip('./')
            img_url = head + tail
            print index
            pic_name = index.replace('/','_') + "#" + name

            dir_path = "photos/" + pic_name + ".jpg"
            with open(dir_path, 'wb') as file_writer:
                conn = urllib2.urlopen(img_url, timeout=0)
                file_writer.write(conn.read())
            file_writer.close()

        except Exception as e:
            print e

        # return item

    def normalWord(self, str):
        if(str != None):
            str = ''.join(str.split())
        return str



