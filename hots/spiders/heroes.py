import json

import scrapy

from ..items import HeroItem


class HeroesSpider(scrapy.Spider):
    name = "heroes"
    start_urls = ["https://heroesofthestorm.com/en-gb/heroes/"]

    def parse(self, response):
        script_with_heroes = response.css(
            'script[type="text/javascript"]::text'
        ).getall()[-1]
        heroes_data = self.get_javascript_data(
            script_with_heroes, "window.blizzard.hgs.heroData"
        )

        new_hero = HeroItem()

        id = 0
        for hero in heroes_data:
            new_hero.id = id
            new_hero.name = hero["name"]
            new_hero.title = hero["title"]
            new_hero.role = hero["expandedRole"]["name"]
            new_hero.type = hero["type"]["name"]
            new_hero.description = hero["description"]
            new_hero.difficulty = hero["difficulty"]
            new_hero.card_portrait = hero["cardPortrait"]
            new_hero.franchise = hero["franchise"]
            new_hero.href = hero["href"]

            id += 1

            yield new_hero

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
