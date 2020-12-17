import sqlite3


class NikkeiPipeline:
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute(f'DROP TABLE if exists news;')

    def process_item(self, item, spider):
        title = item['title'][0]
        description = item['description'][0]
        date = item['date']
        # author = item['author'][0]

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
