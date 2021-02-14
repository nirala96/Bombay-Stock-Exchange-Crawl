# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BseindiascrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Deal_Date = scrapy.Field()
    Security_Code = scrapy.Field()
    Security_Name = scrapy.Field()
    Client_Name = scrapy.Field()
    Deal_Type = scrapy.Field()
    Quantity = scrapy.Field()
    Price = scrapy.Field()

    
