import sqlite3


class NikkeiPipeline:
    conn = sqlite3.connect('Nikkei.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `Nikkei` (
                                    title varchar(100),
                                    description text,
                                    date varchar(25)
                                    )''')
        self.conn.commit()

    def process_item(self, item, spider):

        title = item['title'][0]
        description = item['description'][0]
        date = item['date'][0]
        
        self.cursor.execute(f"""select * from Nikkei
                                        where title = ?
                                        and date = ?""", (title, date))
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            print(title)
            self.cursor.execute(f"""insert into `Nikkei`
                                (`title`, `description`, `date`)
                                values (?, ?, ?)""", (title, description, date))
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
