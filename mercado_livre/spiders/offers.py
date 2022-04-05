import scrapy
from ..items import MercadoLivreItem


class OffersSpider(scrapy.Spider):
    name = 'offers'
    start_urls = ['https://www.mercadolivre.com.br/ofertas']

    def parse(self, response):
        for product_link in response.css('a.promotion-item__link-container::attr(href)'):
            yield response.follow(product_link, callback=self.parse_product)
            
        next_page = response.xpath('//a[contains(@title, "Próxima")]/@href').get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)
    
    def parse_product(self, response):
        name = response.css('h1.ui-pdp-title::text').get()
        categories = response.css('a.andes-breadcrumb__link::text').getall()
        best_seller = response.css('a.ui-pdp-promotions-pill-label__target::text').getall()
        offer_of_the_day = response.css('div.ui-pdp-promotions-pill-label::text').get()
        discount = response.css('span.andes-money-amount__discount::text').get()
        old_price = response.css('span.andes-money-amount__fraction::text').get()
        new_price = response.xpath('//meta[contains(@itemprop, "price")]/@content').get()

        if offer_of_the_day is None:
            offer_of_the_day = False
        else:
            offer_of_the_day = True

        products_item = MercadoLivreItem(
            product_name=name,
            product_categories=categories,
            best_seller=best_seller,
            offer_of_the_day=offer_of_the_day,
            product_discount=discount,
            product_old_price=old_price,
            product_new_price=new_price,
        )

        yield products_item