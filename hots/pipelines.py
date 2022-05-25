import sqlite3


class HotsPipeline:
    def __init__(self):
        self.connection = sqlite3.connect("hots.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS heroes(
            name TEXT PRIMARY KEY,
            title TEXT,
            role TEXT,
            type TEXT,
            description TEXT,
            difficulty TEXT,
            card_portrait TEXT,
            franchise TEXT,
            href TEXT
            )"""
        )

    def process_item(self, item, spider):
        self.cursor.execute(
            """INSERT OR IGNORE INTO heroes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
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
