import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule

from zhihu_spider.items import ZhihuSpiderItem


class ZhihuSpider(RedisCrawlSpider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    redis_key = 'ZhihuSpider:start_urls'
    start_urls = ["https://www.zhihu.com/people/zhi-hui-64-54/activities"]

    rules = (
        Rule(LinkExtractor(allow=(['people/.*/following$',
                                   'people/.*/followers$']), )),
        Rule(LinkExtractor(allow=('www.zhihu.com/people/((?!/).)*$',)),
             callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = ZhihuSpiderItem()
        item['name'] = response.xpath(
            "//*[@class='ProfileHeader-name']/text()").extract_first()
        item['intro'] = response.xpath(
            "//*[@class='ztext ProfileHeader-headline']/text()").extract_first()
        item['detail'] = response.xpath(
            "string(//*[@class='ProfileHeader-info'])").extract_first()
        follow_list = response.xpath(
            "//*[@class='NumberBoard-itemValue']/text()").extract()
        if follow_list:
            item['following'] = follow_list[0]
            item['followers'] = follow_list[1]
        return item
