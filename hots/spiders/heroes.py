import scrapy


class HeroesSpider(scrapy.Spider):
    name = "heroes"
    start_urls = ["https://heroesofthestorm.com/en-gb/heroes/"]

    def parse(self, response):
        pass
