from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from mercado_livre.spiders.offers import OffersSpider

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(OffersSpider)
    process.start()
