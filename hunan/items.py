# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class HunanItem(scrapy.Item):
    pass

class xxgkItem(scrapy.Item):
    index = Field()                        # 索引号
    organization = Field()                 # 所属机构
    department = Field()                   # 公开责任部门
    pubscope = Field()                     # 公开范围
    name = Field()                         # 姓名
    duty = Field()                         # 职务
    work = Field()                         # 工作职责
    resume = Field()                       # 工作简历

