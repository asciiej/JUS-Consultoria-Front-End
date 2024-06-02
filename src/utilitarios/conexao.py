import psycopg2

class PostgreSQLConnection:
    host = "buzutyolmqat5dwhefa2-postgresql.services.clever-cloud.com"
    database = "buzutyolmqat5dwhefa2"
    user = "uxzvrjoyrvfzlsd1rckj"
    password = "wKlpuuKPAOS3c6bRodVc590BRJ14K7"
    port = 50013
    connection = None
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            print("Conexão com o banco de dados estabelecida com sucesso!")
        except psycopg2.Error as e:
            print("Erro ao conectar-se ao banco de dados:", e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")


# Credenciais de conexão

# Criar uma instância da classe de conexão
#db_connection = PostgreSQLConnection()

# Conectar-se ao banco de dados
#db_connection.connect()

# Operações no banco de dados...

# Desconectar-se do banco de dados
#db_connection.disconnect()
