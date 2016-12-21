# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

"""
import json
import codecs

class DoubanbookPipeline(object):
    def __init__(self):
        self.file = codecs.open('result.json',mode='wb',encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))

        return item
"""


import re
from scrapy import log
from twisted.enterprise import adbapi
from DoubanBook.items import DoubanbookItem
import MySQLdb
import MySQLdb.cursors
 
class DoubanbookPipeline(object):
    """docstring for MySQLstor"""
    def __init__(self):
 
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = '127.0.0.1',
            db = 'DoubanBook',
            user = 'root',
            passwd = 'lizoe',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
        )
    def process_item(self, item, spider):
        print spider
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
 
        return item
    def _conditional_insert(self, tx, item):

        if item.get('ISBN'):

            tx.execute("select * from booklist where isbn like '%" + item['ISBN']+"%'")
            dup = tx.fetchone()
            try:
                if dup:
                    print "Found duplicate, updating....."
                    updatesql = "update booklist set title='"+item['title'].replace("'",r"\'")+"', author='"+item['author']+"', translator='"+item['translator']+"', publisher='"+item['publisher']+"', isbn='"+item['ISBN']+"', description='"+item['description'].replace("'",r"\'").replace('(',r'\(').replace(')',r'\)')+"', pic='"+item['pic']+"', category='"+item['category']+"', doubanrating="+item['doubanRating']+", updateat=now() where isbn like '%"+item['ISBN']+"%'"
                    print updatesql
                    tx.execute(updatesql)
            #print item['doubanRating']
            #print item['doubanRating'].strip()
            #print float(item['doubanRating'].strip())
                else:
                    insertsql = "insert into booklist (id, title, author, translator, publisher, isbn, description, pic, category, doubanrating) values (NULL, '" + item['title'].replace("'",r"\'") + "', '" + item['author'] + "', '" + item['translator'] + "', '" + item['publisher'] + "', '" + item['ISBN'] + "', '" + item['description'].replace("'",r"\'").replace('(',r'\(').replace(')',r'\)') + "', '" + item['pic'] + "', '" + item['category'] + "', " + item['doubanRating'] + ")"
                    print insertsql
                    tx.execute(insertsql)
            except Exception,e:
                print e
                

    def handle_error(self, e):
        log.err(e)
