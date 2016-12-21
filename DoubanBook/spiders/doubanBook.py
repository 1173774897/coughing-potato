# -*- coding: utf-8 -*-
import scrapy
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from DoubanBook.items import DoubanbookItem
from urllib import quote
import time


class DoubanbookSpider(scrapy.Spider):
    name = "doubanBook"
    allowed_domains = ["https://book.douban.com"]
    start_urls = (
        'https://book.douban.com/tag/?view=type&icn=index-sorttags-all',
    )

    def parse(self, response):

#        print response.status
#        self.headers=response.headers
#        self.headers['User-Agent']=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6']
#        print self.headers

#        from scrapy.shell import inspect_response
#        inspect_response(response, self)

        for categoryItem in response.xpath('//a[@class="tag-title-wrapper"]/following-sibling::table//a'): 
            category = categoryItem.xpath('../../../../preceding-sibling::a[1]/@name').extract()[0].encode('UTF-8')
            subcategory = categoryItem.xpath('text()').extract()[0]

            subcategoryLink = "https://book.douban.com"+quote(categoryItem.xpath('@href').extract()[0].encode('UTF-8'))

#            yield scrapy.Request(subcategoryLink,
#                                 callback=self.parse_bookitem,
#                                 headers=self.headers,
#                                 dont_filter=True)
            yield scrapy.Request(subcategoryLink,callback=self.parse_bookitem,dont_filter=True,meta={'category':category+"-"+subcategory})





    def parse_bookitem(self,response):

        category = response.meta['category']

        for bookItemURL in response.xpath('//li[@class="subject-item"]//h2/a/@href').extract():

            print "fetched:"+bookItemURL

            yield scrapy.Request(bookItemURL,callback=self.parse_bookitem_details,dont_filter=True,meta={'category':category})

        try:        
            nextPageURL = response.xpath("//span[@class='next']/a/@href").extract()[0].encode('UTF-8')
        except:
            pass
        try:
            if nextPageURL:
                nextPageURL = "https://book.douban.com"+quote(nextPageURL)
                print "going to next page.......: "+nextPageURL
                yield scrapy.Request(bookItemURL,callback=self.parse_bookitem,dont_filter=True,meta={'category':category})
        except:
            pass



    def parse_bookitem_details(self, response):
        print("Visited %s !!!!!!!!!!!!!!!" % response.url)

        item = DoubanbookItem()
 
        item['category'] = response.meta['category']
        try:
            item['title'] = response.xpath('//h1/span/text()').extract()[0].encode("UTF-8").strip()
        except:
            item['title'] = ''

        try:            
            item['pic'] = response.xpath('//div[@id="mainpic"]/a/@href').extract()[0].strip()
        except:
            item['pic'] = ''
 

        au = "作者".decode('UTF-8')
        try:            
            item['author'] = response.xpath("//span[contains(.,'%s')]/following-sibling::a/text()" %au).extract()[0].encode("UTF-8").strip()
        except:
            item['author'] = ''


        pu = "出版社".decode('UTF-8')
        try:            
            item['publisher'] = response.xpath("//span[contains(.,'%s')]/following-sibling::text()" %pu).extract()[0].encode("UTF-8").strip()
        except:
            item['publisher'] = ''


        tr = "译者".decode('UTF-8')
        try:            
            item['translator'] = response.xpath("//span[contains(.,'%s')]/following-sibling::a/text()" %tr).extract()[0].encode("UTF-8").strip()
        except:
            item['translator'] = ''


        try:            
            item['ISBN'] = response.xpath('//span[contains(.,"ISBN")]/following-sibling::text()').extract()[0].strip()
        except:
            item['ISBN'] = ''

        try:            
            item['doubanRating'] = response.xpath('//strong[@class="ll rating_num "]/text()').extract()[0].strip()
        except:
            item['doubanRating'] = ''

        try:            
            item['description'] = ''.join(response.xpath('//div[@class="intro"]//text()').extract()).encode('UTF-8').strip()
        except:
            item['description'] = ''

#        item['updateat'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        return item

        

        


