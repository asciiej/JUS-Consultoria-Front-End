import psycopg2
import config
class PostgreSQLConnection:
    def __init__(self, db_url):
        self.db_url = db_url
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.cursor is None:
            self.connection = psycopg2.connect(self.db_url)
            self.cursor = self.connection.cursor()
            self.connection.set_client_encoding('UTF8')
        return self.cursor, self.connection

    def close(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()
        self.connection = None
        self.cursor = None

    def query(self, query: str, params=None, select=False):

        try:
            self.connect()
            self.cursor.execute(query, params)
            self.connection.commit()
            if not select:
                return self.cursor.fetchall()

            if select:
                colnames = [desc[0] for desc in self.cursor.description]
                results = []
                for row in self.cursor.fetchall():
                    results.append(dict(zip(colnames, row)))
                return results

        except psycopg2.Error as e:
            self.connection.rollback()
            if config.DEBUG:
                print(e)
        finally:
            self.close()

        # try:
        #     self.connect()
        #     self.cursor.execute(query, params)
        #     self.connection.commit()
        #     return self.cursor.fetchall()
        # except psycopg2.Error as e:
        #     self.connection.rollback()
        #     if config.DEBUG:
        #         print(e)
        # finally:
        #     self.close()
