import psycopg2

class PostgreSQLConnection:
    def __init__(self, cfg:dict[str,int]):
        self.host:str = cfg['host']
        self.database:str = cfg['database']
        self.user:str = cfg['user']
        self.password:str = cfg['password']
        self.port:int = cfg['port']
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.cursor is None:
            self.connection = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password, port=self.port)
            self.cursor = self.connection.cursor()
        return self.cursor, self.connection

    def close(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()
        self.connection = None
        self.cursor = None

    def query(self, query:str, params=None):
        try:
            self.connect()
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            self.connection.rollback()
            print(e)
        finally:
            self.close()
