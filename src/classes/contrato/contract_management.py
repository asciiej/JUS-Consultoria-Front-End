import psycopg2

class PostgreSQLConnection:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

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

class Contract:
    def __init__(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.cnae_principal = cnae_principal
        self.cnae_secundario = cnae_secundario
        self.cfop_principais = cfop_principais
        self.industria_setor = industria_setor
        self.receita_anual = receita_anual

class ContractManager:
    def __init__(self, connection):
        self.connection = connection

    def create_contract(self, contract):
        try:
            cursor = self.connection.connection.cursor()
            cursor.execute("INSERT INTO contracts (nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                           (contract.nome_empresa, contract.cnpj, contract.cnae_principal, contract.cnae_secundario, contract.cfop_principais, contract.industria_setor, contract.receita_anual))
            self.connection.connection.commit()
            cursor.close()
            print("Contrato criado com sucesso!")
        except psycopg2.Error as e:
            print("Erro ao criar contrato:", e)

    # Métodos de leitura, atualização e deleção aqui...

# Exemplo de uso:

# Credenciais de conexão
host = "buzutyolmqat5dwhefa2-postgresql.services.clever-cloud.com"
database = "buzutyolmqat5dwhefa2"
user = "uxzvrjoyrvfzlsd1rckj"
password = "wKlpuuKPAOS3c6bRodVc590BRJ14K7"
port = 50013

# Criar uma instância da classe de conexão
db_connection = PostgreSQLConnection(host, database, user, password, port)

# Conectar-se ao banco de dados
db_connection.connect()

# Criar uma instância da classe ContractManager com a conexão
contract_manager = ContractManager(db_connection)

# Criar um novo contrato
new_contract = Contract(nome_empresa="Empresa A", cnpj="123456789", cnae_principal="1234", cnae_secundario="5678", cfop_principais="9012", industria_setor="Indústria", receita_anual=1000000)
contract_manager.create_contract(new_contract)

# Operações adicionais no banco de dados...

# Desconectar-se do banco de dados
db_connection.disconnect()
