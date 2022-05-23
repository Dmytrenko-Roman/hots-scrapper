import scrapy
import json


class HeroesSpider(scrapy.Spider):
    name = "heroes"
    start_urls = ["https://heroesofthestorm.com/en-gb/heroes/"]

    def parse(self, response):
        script_with_heroes = response.css("script[type=\"text/javascript\"]::text").getall()[-1]
        heroes_data = self.get_javascript_data(script_with_heroes, "window.blizzard.hgs.heroData")

        for hero in heroes_data:
            yield hero

    def get_javascript_data(self, html: str, variable_name: str) -> json:
        """
        get_javascript_data finds variable in javascript data.

        :param html: string to find data
        :param variable_name: name of the variable to find
        :return: json
        """

        start_from = html.index("=", html.index(variable_name)) + 1
        ends_on = html.index("];", html.index(variable_name)) + 1

        data = json.loads(html[start_from:ends_on])
        return data
