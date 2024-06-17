from ...utilitarios.excecoes import usuarioOuSenhaInválido
from ...utilitarios.local_user import local_user
import config
class UsuarioModel:
    def __init__(self, nome: str, sobrenome: str, cpf:str, nomeEmpresa:str, cargo:str, email: str, telefone: str, pais: str, roles:tuple):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.nomeEmpresa = nomeEmpresa
        self.cargo = cargo
        self.email = email
        self.telefone = telefone
        self.pais = pais
        self.roles = roles

    def str(self) -> str:
        return (f"Nome: {self.nome} {self.sobrenome}\n"
                f"Cargo: {self.cargo if self.cargo is not None else 'Não informado'}\n"
                f"E-mail: {self.email}\n"
                f"Telefone: {self.telefone}\n"
                f"País/Localização: {self.pais}")

# TODO: Tratar erros em todos os metodos
class UsuarioManager:
    def __init__(self, db):
        self.db = db

    def login(self,email,senha):
        try:
            retornoBD = self.get_by_email(email)
        except Exception as e:
            if config.DEBUG:
                print("Erro ao efeiturar login: ",e)

        if len(retornoBD) == 0:
            raise usuarioOuSenhaInválido()

        retornoBD = retornoBD[0]
        if retornoBD[9] != senha:
            raise usuarioOuSenhaInválido()

        return UsuarioModel(nome = retornoBD[1], sobrenome = retornoBD[2],cpf = retornoBD[3], nomeEmpresa = retornoBD[4],cargo = retornoBD[5],email = retornoBD[6], telefone = retornoBD[7], pais = retornoBD[8], roles=retornoBD[9])

    # (2, 'Carlos', 'Santos', '987.654.321-00', 'SimCorp', 'Engenheiro de Cozinha', 'carlos.santos@example.com', '+55 12 34567-8901', 'EUA', '07cd109ac902429f267f8279f2a0041c')

    def create(self, nome:str, sobrenome:str, cpf:str, nomeEmpresa:str, cargo:str, email:str, telefone:str, pais:str, senha:str):
        print(self.get_by_cpf(cpf))
        if self.get_by_cpf(cpf):
            return 'CPF ja cadastrado'

        query = """
            INSERT INTO users.clients (nome, sobrenome, cpf, nome_empresa, cargo, email, telefone, pais, senha)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING *;
            """
        params = (nome, sobrenome, cpf, nomeEmpresa, cargo, email, telefone, pais, senha)
        return self.db.query(query, params)

    def get_all(self):
        query = "SELECT * FROM users.clients"
        return self.db.query(query)

    def get_by_cpf(self, cpf:str):
        query = "SELECT * FROM users.clients WHERE cpf = %s"
        result = self.db.query(query, (cpf,))
        if result:
            return result[0]
        return None

    def get_by_email(self, email:str):
        query = "SELECT * FROM users.clients WHERE email = %s"
        result = self.db.query(query, (email,))
        if result:
            return result[0]
        return None

    def get_roles(self, cpf:str):
        user = self.get_by_cpf(cpf)
        return user[10]

    def has_role(self, cpf:str, role:str):
        user = self.get_by_cpf(cpf)
        if user:
            return role in user[10]

    def add_role(self, cpf: str, role: str):
        user = self.get_by_cpf(cpf)

        if user:
            query = """
                UPDATE users.clients
                SET roles = array_append(roles, %s)
                WHERE cpf = %s
                """
            params = (role, cpf)
            self.db.query(query, params)

        return self.get_by_cpf(cpf)

    def remove_role(self, cpf:str, role:str):
        user = self.get_by_cpf(cpf)

        if user:
            query = """
                UPDATE users.clients
                SET roles = array_remove(roles, %s)
                WHERE cpf = %s
                """
            params = (role, cpf)
            self.db.query(query, params)

        return self.get_by_cpf(cpf)


    def update(self, cpf:str,nome:str,sobrenome:str,nomeEmpresa:str,cargo:str,email:str,telefone:str,pais: str,senha:str):
        user = self.get_by_cpf(cpf)
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
                    senha = %s,
                WHERE cpf = %s
                """
            params = (nome, sobrenome, nomeEmpresa, cargo, email, telefone, pais, senha, cpf)
            self.db.query(query, params)
        return self.get_by_cpf(cpf)

    def delete(self, cpf:str):
        user = self.get_by_cpf(cpf)
        if user:
            query = "DELETE FROM users.clients WHERE cpf = %s"
            self.db.query(query, (cpf,))
        return self.get_by_cpf(cpf)