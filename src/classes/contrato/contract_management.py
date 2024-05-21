import psycopg2
from src.utilitarios.conexao import PostgreSQLConnection

class contractManager:
    def __init__(self):
        self.connection = PostgreSQLConnection()

    def listaContratos(self):
        try:
            self.connection.connect()
            cursor = self.connection.connection.cursor()
            cursor.execute(f"SELECT * FROM JUSConsultoria.modeloDeContrato;")
            self.connection.connection.commit()
            retornoBD = cursor.fetchall()
            cursor.close()
        except psycopg2.Error as e:
            print("Erro ao efeiturar login: ",e)
        finally:
            self.connection.disconnect()
        
        return retornoBD
    

print(contractManager().listaContratos())