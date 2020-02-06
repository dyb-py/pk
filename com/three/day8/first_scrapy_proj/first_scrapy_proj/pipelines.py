# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

conn = MySQLdb.connect(host='localhost',port=3306,user='root',password='123456',db='biquge_zhangjie',charset='utf8')
cursor = conn.cursor()
class FirstScrapyProjPipeline(object):
    def process_item(self, item, spider):
        zhangjie = item['zhangjie']
        sql = 'INSERT INTO zhangjie VALUES (%s)'
        cursor.execute(sql,(zhangjie,))
        conn.commit()
        return item
