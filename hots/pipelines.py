import sqlite3


class HotsPipeline:
    def __init__(self):
        self.connection = sqlite3.connect("../hots.db")
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """INSERT OR IGNORE INTO heroes_hero VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                item.id,
                item.name,
                item.title,
                item.role,
                item.type,
                item.description,
                item.difficulty,
                item.card_portrait,
                item.franchise,
                item.href,
            ),
        )
        self.connection.commit()

        return item
