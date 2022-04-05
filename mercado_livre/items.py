# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadoLivreItem(scrapy.Item):
    # define the fields for your item here like:
    # name  ()
    product_name = scrapy.Field()
    product_categories = scrapy.Field()
    best_seller = scrapy.Field() 
    offer_of_the_day = scrapy.Field() 
    product_discount = scrapy.Field()
    product_old_price = scrapy.Field()
    product_new_price = scrapy.Field() 
    pass
