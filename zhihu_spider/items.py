# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuSpiderItem(scrapy.Item):
    name = scrapy.Field()       # 姓名(昵称)
    intro = scrapy.Field()      # 自我介绍
    detail = scrapy.Field()     # 详细资料
    following = scrapy.Field()  # 关注人数
    followers = scrapy.Field()  # 粉丝数

