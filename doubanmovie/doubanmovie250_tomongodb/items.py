# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubanmovie250TomongodbItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    star = scrapy.Field()
    summary = scrapy.Field()
    
    #title://div[@id='content']/h1/span[1]/text()
    #year://div[@id='content']/h1/span[2]/text()
    #director://div[@id='info']/span[1]/span[2]/a/text()
    #star://strong/text()
    #summary://span[@property='v:summary']/text()     [0]
    
    
    
    
    
    

