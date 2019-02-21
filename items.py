# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WellsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    well_api = scrapy.Field()
    well_status = scrapy.Field()
    country_name = scrapy.Field()
    lease_name = scrapy.Field()
    operator = scrapy.Field()
    production_table = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    spud_date = scrapy.Field()
