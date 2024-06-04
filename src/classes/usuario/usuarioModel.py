from ...utilitarios.excecoes import usuarioOuSenhaInválido
from ...utilitarios.local_user import local_user
import config
class UsuarioModel:
    def __init__(self, nome: str, sobrenome: str, cpf:str, nomeEmpresa:str, cargo:str, email: str, telefone: str, pais: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone
        self.pais = pais
        self.cargo = cargo
        self.nomeEmpresa = nomeEmpresa
        self.cpf = cpf

    def str(self) -> str:
        return (f"Nome: {self.nome} {self.sobrenome}\n"
                f"Cargo: {self.cargo if self.cargo is not None else 'Não informado'}\n"
                f"E-mail: {self.email}\n"
                f"Telefone: {self.telefone}\n"
                f"País/Localização: {self.pais}")

class UsuarioManager:
    def __init__(self, db):
        self.db = db

    def login(self,email,senha):
        try:
            retornoBD = self.getUserByEmail(email)
        except Exception as e:
            if config.DEBUG:
                print("Erro ao efeiturar login: ",e)

        if len(retornoBD) == 0:
            raise usuarioOuSenhaInválido()

        retornoBD = retornoBD[0]
        if retornoBD[7] != senha:
            raise usuarioOuSenhaInválido()

        return UsuarioModel(retornoBD[1],retornoBD[2],retornoBD[4],retornoBD[5],retornoBD[6],retornoBD[3],cpf = None)

    # Metodos de Criação

    def cadastroUsuario(self,nome:str,sobrenome:str,cpf:str,nomeEmpresa:str,cargo:str,email:str,telefone:str,pais: str,senha:str):
        try:
            return self.db.query(
                f"""
                    INSERT INTO users.clients (nome, sobrenome, cpf, nome_empresa, cargo, email, telefone, pais, senha)
                    VALUES ('{nome}', '{sobrenome}', '{cpf}', '{nomeEmpresa}', '{cargo}', '{email}', '{telefone}', '{pais}', '{senha}');
                """)
        except Exception as e:
            if config.DEBUG:
                print("Erro ao cadastrar usuário no Banco de Dados", e)

    # Métodos de leitura, atualização e deleção aqui...

    def getUserByCPF(self, cpf:str):
        query = "SELECT * FROM users.clients WHERE cpf = %s"
        result = self.db.query(query, (cpf,))
        if result:
            return result[0]
        return None

    def getUserByEmail(self, email:str):
        query = "SELECT * FROM users.clients WHERE email = %s"
        result = self.db.query(query, (email,))
        if result:
            return result[0]
        return None

    def alterarDadosUsuario(self, cpf:str,nome:str,sobrenome:str,nomeEmpresa:str,cargo:str,email:str,telefone:str,pais: str,senha:str):
        user = self.getUserByCPF(cpf)
        if user:
            query = """
                UPDATE users.clients
                SET nome = %s,
                    sobrenome = %s,
                    nome_empresa = %s,
                    cargo = %s,
                    email = %s,
                    telefone = %s,
                    pais = %s,
                    senha = %s
                WHERE cpf = %s
                """
            params = (nome, sobrenome, nomeEmpresa, cargo, email, telefone, pais, senha, cpf)
            self.db.query(query, params)
        return self.getUserByCPF(cpf)
