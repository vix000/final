# -*- coding: utf-8 -*-
import time

import scrapy
import re
from scrapy_splash import SplashRequest, SplashFormRequest, SplashResponse
from selenium import webdriver
from scrapy.selector import HtmlXPathSelector

class Zalando(scrapy.Spider):

    name = 'restaurant'


    def start_requests(self):

        self.script = """
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(0.5))
          assert(splash:set_viewport_full())
          return {
            html = splash:html(),
            har = splash:har(),
          }
        end
            """
        self.tag = getattr(self, 'tag', None).replace(" ","+")
        # self.tag = "Sushi+Gdansk"
        self.url = f"https://www.google.com/maps/search/restauracja+{self.tag}"
        if self.tag:
            yield SplashRequest(self.url, self.search, args={'har': 1,
                'html': 1,
                'lua_source': self.script,
                'wait' : 0.5,})
        else:
            raise AttributeError("You need to write city and type of restaurant")

    def search(self,response):
        for restaurant in response.xpath('//h3[contains(@class,"title")]/span/text()'):
            yield SplashRequest(
                'https://www.google.com/maps/search/restauracja+' + f"{restaurant.extract().replace(' ', '+')}+Gdynia Maksymiliana",
                self.after_search, endpoint='execute', args={'har': 1,
                'html': 1,
                'lua_source': self.script,
                'wait' : 0.5,}
            )

    def after_search(self, response):

        website =response.xpath("//span[contains(@class,'section-info-text')]").extract()
        print("-----------------------------------")
        print(website)
        print("-----------------------------------")
        if website is not []:
            yield SplashRequest(
                      'http://'+''.join(website)+"/menu",
                      self.restWebsite,
                      endpoint='execute',
                      args={'har': 1,
                      'html': 1,
                      'lua_source': self.script,
                      'wait' : 0.5,}
                      )

    def restWebsite(self, response):
        print("0000000000000000000000000000000000")
        print("0000000000000000000000000000000000")
        print("0000000000000000000000000000000000")
        print(response.xpath('//div[contains(text(),"PIZZA")]'))
    #     links = set()
    #     tag = self.tag.lower()
    #     for href in response.xpath(f'//a[contains(@href, "{tag}")]/@href').extract():
    #         links.add(href)
    #     for link in links:
    #         yield SplashRequest(response.urljoin(link),self.item, args={'lua_source': self.script})
    #
    # def item(self, response):
    #     link = response.xpath('//a[contains(text(),"więcej")]/@href')[-1].extract()
    #     yield SplashRequest(link,self.seeMore, args={'lua_source': self.script})
    #
    # def seeMore(self, response):
    #     for index, item in enumerate(response.xpath("//img")):
    #         itemName =item.xpath('@alt').extract_first(),
    #         itemImg = item.xpath('@src[contains(.,"jpg")]').extract_first()
    #         url = item.xpath(f'//a[contains(@href,".html")]/@href')[index].extract()
    #         price = item.xpath('//span[contains(text(),"zł")]/text()')[index].extract()
    #         if itemImg is not None and itemName is not None and "None" not in str(itemName) and price is not None and url is not None:
    #             if re.search(f"{self.tag.upper()}",str(itemName)):
    #                 continue
    #             else:
    #                 yield {
    #                     "".join(str(itemName)): {
    #                         "image":itemImg,
    #                         "price": price,
    #                         "url": url
    #
    #                     }
    #                 }
        # >> > response.xpath('//a[contains(text(),"więcej")]/@href')[-1].extract()

        # for href in response.css("div.pagination a::attr(href)"):
        #     yield response.follow(href, self.parse)