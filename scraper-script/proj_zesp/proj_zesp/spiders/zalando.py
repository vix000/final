# -*- coding: utf-8 -*-
import time

import scrapy
import re
from scrapy_splash import SplashRequest, SplashFormRequest, SplashResponse
from scrapy.selector import HtmlXPathSelector

class Zalando(scrapy.Spider):

    name = 'clothing'


    def start_requests(self):

        self.script = """
          function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(0.5))
          assert(splash:set_viewport_full())
          return {
            html = splash:html()}
            end
            """
        urls = ["https://reserved.com/pl/pl","https://zalando.pl","https://domodi.pl"]
        self.limit = 50
        self.tag = getattr(self, 'tag', None).split(" ")
        for self.url in urls:
            if self.tag is not None:
                yield SplashRequest(self.url, self.search)
            else:
                raise AttributeError("Tag is missing")

    def search(self, response):
        if "domodi" in str(response):
            form_name = response.xpath('//input/@name').extract()[1]
        else:
            form_name = response.xpath('//input/@name').extract_first()
        return SplashFormRequest.from_response(
            response,
            formdata={form_name:" ".join(self.tag)},
            callback=self.after_search,
        )
     
    def after_search(self, response):

        links = set()
        tag = self.tag[0].lower()
        counter = 0
        for href in response.xpath(f'//a[contains(@href, "{tag}")]/@href').extract():
            links.add(href)
        for href in response.xpath("//a[./img[contains(@src,.)]]/@href").extract():
            links.add(href)
        for link in links:
            counter += 1
            if counter < self.limit:
                yield SplashRequest(response.urljoin(link),self.item,args={'har': 1,
                    'html': 1,
                    'lua_source': self.script,
                    'wait' : 0.5})
            else:
                return

    def item(self, response):
        if "domodi" in str(response):
            for item in response.xpath("//li"):
                itemImg = item.xpath('.//a[contains(@href,"przejdz?")]/img/@src').extract()
                itemName = item.xpath('.//a[contains(@href,"przejdz?")]/img/@alt').extract()
                price = item.xpath('.//span[not(contains(@class,"old")) and contains(text(),"zł")]/text()').extract()
                url = "https://domodi.pl/" + "".join(item.xpath('.//a[contains(@href,"przejdz?")]/@href').extract())
                
                if itemImg is not None and itemName is not None and "None" not in str(itemName) and price is not None and url is not None and itemName is not "[]" and itemImg != []:
                    yield {
                        "".join(itemName): {
                        "image":"".join(itemImg).replace("//",""),
                        "price":"".join(price),
                        "url": "".join(url)}
                            }

        elif "zalando" in str(response):
            counter = 0
            try:
                link = response.xpath('//a[contains(text(),"więcej")]/@href')[-1].extract()
                counter += 1
                if counter < self.limit:
                    yield SplashRequest(link,self.seeMoreZalando, args={'lua_source': self.script})
                else:
                    return
            except IndexError:
                pass
        elif "reserved" in str(response):
            for item in response.xpath("//div[contains(@class,'portrait')]"):
                itemImg = item.xpath(".//div[contains(@class, 'photo')]/a/img/@src").extract()
                itemName = item.xpath(".//div[contains(@class, 'photo')]/a/img/@alt").extract()
                price = item.xpath(".//p[@class='price']/span[contains(text(),'PLN')]/text()").extract_first()
                url = item.xpath(".//div[contains(@class, 'photo')]/a/@href").extract()

                if itemImg is not None and itemName is not None and "None" not in str(itemName) and price is not None and url is not None and itemName is not "[]" and itemImg != []:
                    counter += 1
                    yield {
                        "".join(itemName): {
                        "image":"".join(itemImg),
                        "price": "".join(price.split()),
                        "url": "".join(url)}
                            }
        else:
            pass

    def seeMoreZalando(self, response):
        for item in response.xpath("//div[./a[contains(@href,'zalando.pl')]]"):
            url = item.xpath('./a/@href').extract()
            itemImg = item.xpath('.//*/img[contains(@src,.)]/@src').extract()
            pricePath = item.xpath(".//a/div/span[contains(text(),'zł')]/text()")
            price = item.xpath(".//span[contains(text(),'zł')]/text()").extract_first()
            itemName = item.xpath('.//*/img[contains(@src,.)]/@alt').extract()

            if itemImg is not None and itemName is not None and "None" not in str(itemName) and price is not None and url is not None and itemName is not "[]" and itemImg != []:
                yield {
                    "".join(itemName): {
                        "image":"".join(itemImg),
                        "price": price,
                        "url": "".join(url)
                    }
                }
