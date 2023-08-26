# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
from pymongo import MongoClient

class ZhihuSpiderPipeline:
    # 在open_spider方法中链接MongDB,创建数据库和集合
    def open_spider(self, spider):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['zhihu_db']
        self.collection = self.db['zhihu_collection']

    # 定义process_item方法
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item

    # 在spider关闭的同时关闭连接
    def close_spider(self, spider):
        self.client.close()

