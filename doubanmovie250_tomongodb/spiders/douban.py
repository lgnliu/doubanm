# -*- coding: utf-8 -*-
import scrapy
from doubanmovie250_tomongodb.items import Doubanmovie250TomongodbItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = 'https://movie.douban.com/top250?start='
    start_urls = [url + str(offset)]
    
    # 处理所有页面的url
    def parse(self, response):
        # 获取第一个页面的url列表
        links = response.xpath("//div[@class='hd']/a/@href").extract()
        for link in links:
            # 一个页面上的url，逐个发送给parse_item方法处理
            yield scrapy.Request(link, callback=self.parse_item)
            
        # 页码递增一次，并返回给self.parse继续获取下一页面的url列表        
        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
        
    
    # 处理二级页面内容
    def parse_item(self, response):
        item = Doubanmovie250TomongodbItem()
        if response.xpath("//div[@id='content']/h1/span[1]/text()"):
            item['title'] = response.xpath("//div[@id='content']/h1/span[1]/text()").extract()[0]
        else:
            item['title'] = 'None'
        if response.xpath("//div[@id='content']/h1/span[2]/text()"):
            item['year'] = response.xpath("//div[@id='content']/h1/span[2]/text()").extract()[0]
        else:
            item['year'] = 'None'
        if response.xpath("//div[@id='info']/span[1]/span[2]/a/text()"):
            item['director'] = response.xpath("//div[@id='info']/span[1]/span[2]/a/text()").extract()[0]
        else:
            item['director'] = 'None'
        if response.xpath("//strong/text()"):
            item['star'] = response.xpath("//strong/text()").extract()[0]
        else:
            item['star'] = 'None'
        if response.xpath("//span[@property='v:summary']/text()"):
            item['summary'] = response.xpath("normalize-space(//span[@property='v:summary']/text())").extract()[0]
        else:
            item['summary'] = 'None'
        
        yield item
    
    
    
