from ...utilitarios.excecoes import usuarioOuSenhaInválido
class UsuarioModel:
    def __init__(self, nome: str, sobrenome: str, email: str, telefone: str, pais: str, cargo:str,cpf:str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone
        self.pais = pais
        self.cargo = cargo
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

    def login(self,eMail,senha):
        try:
            retornoBD = self.getUserByEmail(eMail)
        except Exception as e:
            print("Erro ao efeiturar login: ",e)

        if len(retornoBD) == 0:
            raise usuarioOuSenhaInválido()

        retornoBD = retornoBD[0]
        if retornoBD[7] != senha:
            raise usuarioOuSenhaInválido()

        return UsuarioModel(retornoBD[1],retornoBD[2],retornoBD[4],retornoBD[5],retornoBD[6],retornoBD[3],cpf = None)

    # Metodos de Criação

    def cadastroUsuario(self,nome:str,sobrenome:str,cpf:str,nomeEmpresa:str,cargo:str,eMail:str,telefone:str,pais: str,senha:str):
        try:
            self.db.query(f"INSERT INTO JUSConsultoria.usuario (nome, sobrenome, cargo, email, numeroTelefone, paisLocalizacao, senha, empresa_id, informacoesPessoaisContrato_idinformacoesPessoaisContrato) VALUES ('{nome}', '{sobrenome}', '{cargo}', '{eMail}', '{telefone}', '{pais}', '{senha}', 1, 1);")
        except Exception as e:
            print("Erro ao cadastrar usuário no Banco de Dados", e)

    # Métodos de leitura, atualização e deleção aqui...

    def getUserByEmail(self, email:str):
        return self.db.query(f"SELECT * FROM JUSConsultoria.usuario WHERE email = '{email}';")

