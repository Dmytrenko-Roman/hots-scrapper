# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class HotsPipeline:
    def __init__(self):
        self.connection = sqlite3.connect("hots.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS heroes(
                name TEXT PRIMARY KEY,
                title TEXT,
                role TEXT,
                type TEXT,
                description TEXT,
                difficulty TEXT,
                card_portrait TEXT,
                franchise TEXT,
                href TEXT,
            )
            """
        )

    def process_item(self, item, spider):
        return item
