# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KuaidailiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    position_ip = scrapy.Field()
    position_port = scrapy.Field()
    position_niming = scrapy.Field()
    position_yp = scrapy.Field()
    position_loc = scrapy.Field()
    position_spe = scrapy.Field()
    position_time = scrapy.Field()
