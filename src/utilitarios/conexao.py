import psycopg2

class Database:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database!")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database.")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")

    def fetch_data(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except psycopg2.Error as e:
            print(f"Error fetching data: {e}")

# Exemplo de uso:
if __name__ == "__main__":
    db = Database(
        host="buzutyolmqat5dwhefa2-postgresql.services.clever-cloud.com",
        database="buzutyolmqat5dwhefa2",
        user="uxzvrjoyrvfzlsd1rckj",
        password="wKlpuuKPAOS3c6bRodVc590BRJ14K7",
        port="50013"
    )

    db.connect()

    # Exemplo de execução de consulta
    query = "SELECT * FROM sua_tabela;"
    data = db.fetch_data(query)
    print(data)

    db.disconnect()
