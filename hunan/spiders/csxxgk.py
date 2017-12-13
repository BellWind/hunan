# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from scrapy import Request
import urllib
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class CsxxgkSpider(scrapy.Spider):
    name = 'csxxgk'
    # allowed_domains = ['www.changsha.gov.cn']
    start_urls = ['http://www.changsha.gov.cn/xxgk/szfxxgkml/#chnl227']

    def parse(self, response):
        sel = Selector(response)
        head = "http://www.changsha.gov.cn/xxgk/"
        url = head + sel.xpath("/html/body/div[2]/div/div[2]/div/div[3]/div[1]/ul/li[2]/dl[1]/dt/span/a[1]/@href").extract_first().lstrip('../')
        yield Request(url, callback=self.parse2)

    def parse2(self, response):
        sel = Selector(response)
        url = response.url + sel.xpath('//*[@id="deptFileList"]/li[1]/ul/li[1]/a/@href').extract_first().lstrip('./')
        yield Request(url, callback=self.parse3)

    def parse3(self, response):
        sel = Selector(response)
        path = '//*[@class="docTitle_link"]/@href'
        urls = sel.xpath(path).extract()

        for url in urls:
            url = response.url + url.lstrip('./')
            yield Request(url, callback=self.parse4)

    def parse4(self, response):
        sel = Selector(response)
        path = '//img/@src'
        pattern = re.compile('http://www.changsha.gov.cn/xxgk/.*/', re.S)
        head = re.findall(pattern, response.url)[0]
        tail = sel.xpath(path).extract_first().lstrip('./')
        img_url = head + tail
        dir_path = "phototest/" + tail
        with open(dir_path, 'wb') as file_writer:
            conn = urllib.urlopen(img_url)  # 下载图片
            file_writer.write(conn.read())
        file_writer.close()


