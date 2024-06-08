from ...utilitarios.conexao import PostgreSQLConnection
from .usuarioModel import usuarioModel
from ...utilitarios.excecoes import usuarioOuSenhaInválido
import psycopg2

class usuarioManager:
    def __init__(self):
        self.connection = PostgreSQLConnection()

    def login(self,eMail,senha):
        try:
            self.connection.connect()
            cursor = self.connection.connection.cursor()
            cursor.execute(f"SELECT * FROM JUSConsultoria.usuario WHERE email = '{eMail}';")
            self.connection.connection.commit()
            retornoBD = cursor.fetchall()
            cursor.close()
        except psycopg2.Error as e:
            print("Erro ao efeiturar login: ",e)
        finally:
            self.connection.disconnect()

        if len(retornoBD) == 0:
            raise usuarioOuSenhaInválido()
        
        retornoBD = retornoBD[0]
        if retornoBD[7] != senha:
            raise usuarioOuSenhaInválido()
        
        return usuarioModel(retornoBD[1],retornoBD[2],retornoBD[4],retornoBD[5],retornoBD[6],retornoBD[3],cpf = None)
    
    def cadastroUsuario(self,nome:str,sobrenome:str,cpf:str,nomeEmpresa:str,cargo:str,eMail:str,telefone:str,pais: str,senha:str):
        try:
            self.connection.connect()
            cursor = self.connection.connection.cursor()
            cursor.execute(f"INSERT INTO JUSConsultoria.usuario (nome, sobrenome, cargo, email, numeroTelefone, paisLocalizacao, senha, empresa_id, informacoesPessoaisContrato_idinformacoesPessoaisContrato) VALUES ('{nome}', '{sobrenome}', '{cargo}', '{eMail}', '{telefone}', '{pais}', '{senha}', 1, 1);")  
            self.connection.connection.commit()
            cursor.close()
        except psycopg2.Error as e:
            print("Erro ao cadastrar usuário no Banco de Dados: ",e)
        finally:
            self.connection.disconnect()

    # Métodos de leitura, atualização e deleção aqui...