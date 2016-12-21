# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    translator = scrapy.Field()
    publisher = scrapy.Field()

    ISBN = scrapy.Field()
    pic = scrapy.Field()
    description = scrapy.Field()

    doubanRating = scrapy.Field()
    category = scrapy.Field()

    #updateat = scrapy.Field()

