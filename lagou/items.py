# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    companyName = scrapy.Field()
    companySize = scrapy.Field()
    positionName = scrapy.Field()
    salaryMax = scrapy.Field()
    salaryMin = scrapy.Field()
    salaryAvg = scrapy.Field()
    positionType = scrapy.Field()
    positionAdvantage = scrapy.Field()
    companyLabelList = scrapy.Field()
    companyLogo = scrapy.Field()
    workYear = scrapy.Field()  # 工作年限
    education = scrapy.Field() #教育经历
    jobNature = scrapy.Field() # 全职还是兼职
    financeStage = scrapy.Field() #成长型/c轮/d轮
    district = scrapy.Field() # 朝阳区
    deliverCount = scrapy.Field() # 交付统计 已提交简历
    createTime = scrapy.Field() # 创建时间
    industryField = scrapy.Field() # 行业
    showCount = scrapy.Field() # 被查看次数
    positionId = scrapy.Field() # 职位id：positionId
    pvScore = scrapy.Field()

