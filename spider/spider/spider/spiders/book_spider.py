#!/usr/bin/python
#coding=utf-8

import scrapy

class BooksSpider(scrapy.Spider):
    #spider name
    name = 'books'
    # start point
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.css('p.price_color::text').extract_first()
            yield {'name': name, 'price': price}
            next_url = response.css('url.pager li.next a::attr(href)').extract_first()
            if next_url:
                next_url = response.urljoin(next_url)
                yield scrapy.Request(next_url, callback=self.parse)

