# -*- coding: utf-8 -*-
import scrapy
import time

class SahibindenspiderSpider(scrapy.Spider):
    name = 'sahibindenSpider'
    allowed_domains = ['www.sahibinden.com']
    start_urls = ['https://www.sahibinden.com/otomobil/?pagingOffset=%s' % page for page in range(0,20,20)]

    def parse(self, response):
        crawled_models=response.xpath("//form[@id='searchResultsSearchForm']//div[@class='searchResultsRight']//tr//td[@class='searchResultsTagAttributeValue']/text()").extract()
        crawled_attributes=response.xpath("//form[@id='searchResultsSearchForm']//div[@class='searchResultsRight']//tr//td[@class='searchResultsAttributeValue']/text()").extract()
        prices=response.xpath("//form[@id='searchResultsSearchForm']//div[@class='searchResultsRight']//tr//td[@class='searchResultsPriceValue']//div/text()").extract()
        #urls=response.xpath("//form[@id='searchResultsSearchForm']//div[@class='searchResultsRight']//tr//td[@class='searchResultsLargeThumbnail']//@href").extract()

        brands=[]
        serials=[]
        models=[]
        years=[]
        KMs=[]
        colors=[]
        for i in range(0,int(len(crawled_models)-2),3):
            brands.append(crawled_models[i].strip())
            serials.append(crawled_models[i+1].strip())
            models.append(crawled_models[i+2].strip())

        for i in range(0,int(len(crawled_attributes)-2),3):
            years.append(crawled_attributes[i].strip())
            KMs.append(crawled_attributes[i+1].strip())
            colors.append(crawled_attributes[i+2].strip())

        for i in range(len(models)):
            prices[i]=prices[i].strip()
            yield{
                "Brand":brands[i],
                "Serial": serials[i],
                "Model": models[i],
                "Year":years[i],
                "KM": KMs[i],
                "Color": colors[i],
                "Price":prices[i]
            }