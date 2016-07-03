# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# setting设置类比django
# 去重 http://scrapy-chs.readthedocs.io/zh_CN/1.0/topics/item-pipeline.html#id3
# 参考 https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/

from scrapy.conf import settings
import pymongo


class LagouMongodbPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DB_NAME']
        collection = settings['MONGODB_COLLECTION']
        connection = pymongo.MongoClient(host, port)
        db = connection[dbname]
        self.collection = db[collection]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))  #json变为字典，可以做些清洗校验工作
        return item
