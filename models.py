import pymysql

class Connection:

    def connect(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='1149',
            db='flask-api'
        )

        self.cursor = self.conn.cursor()

    def execute(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            data = self.cursor.fetchall()
        except Exception as e:
            self.connect()
            self.cursor.execute(query)
            self.conn.commit()
            data = self.cursor.fetchall()
        finally:
            self.conn.close()

        return data
