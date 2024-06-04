from ...utilitarios.excecoes import cargoInválido, eMailInválido, nomeInválido, paisInválido, cpfInválido, nomeEmpresaInválido, senhaInválido, telefoneInválido
from ...utilitarios.check import Check
from ...utilitarios.local_user import local_user
import config
import hashlib

class UsuarioControler():
    def __init__(self, usuario_manager):
        self.usuario_manager = usuario_manager

    def login(self,eMail:str,senha:str):

        if not Check.EMail(eMail):
            raise eMailInválido(eMail)

        if ' ' in senha:
            raise senhaInválido()

        senha = self._calcularMd5(senha)

        #Implementar a funcionalidade de login do crud]
        try:
            local_user['user'] = self.usuario_manager.login(eMail,senha)
            local_user['logged'] = True
        except Exception as e:
            if config.DEBUG:
                print(e)
            return False
        return True
        #return (true or false) se o usuário for encontrado no banco ou não


    def cadastro(self,nome:str,sobrenome:str,cpf:str,nomeEmpresa:str,cargo:str,eMail:str,telefone:str,pais: str,senha:str,confirmeSenha:str):

        if not Check.Nome(nome,sobrenome):
            raise nomeInválido(nome,sobrenome)

        if not Check.EMail(eMail):
           raise eMailInválido(eMail)

        # Telefones precisam ter código de país, código de area e o prefixo 9, indicando um telefone celular. Exemplo de telefone válido: cc (cc) c cccc-cccc
        if not Check.Telefone(telefone):
            raise telefoneInválido(telefone)

        if not Check.String(cargo):
            raise cargoInválido(cargo)

        if not Check.String(nomeEmpresa):
            raise nomeEmpresaInválido(nomeEmpresa)

        if not Check.String(pais):
            raise nomeEmpresaInválido(nomeEmpresa)

        if not Check.Senha(senha,confirmeSenha):
            raise senhaInválido()

        # cpf obrigatóriamente no formato 111.111.111-11
        if not Check.CPF(cpf):
            raise cpfInválido(cpf)

        senha = self._calcularMd5(senha) #converter a senha para hash md5 que será armazenado no banco de dados

        # aqui usamos as funcionalidades do model para inserir este usuário no banco de dados
        self.usuario_manager.cadastroUsuario(nome, sobrenome, cpf, nomeEmpresa, cargo, eMail, telefone, pais, senha)

    def _calcularMd5(self,texto):
        # Codifica o texto em bytes antes de calcular o hash MD5
        texto_codificado = texto.encode('utf-8')

        # Calcula o hash MD5
        md5_hash = hashlib.md5(texto_codificado)

        # Retorna o hash MD5 como uma string hexadecimal
        return md5_hash.hexdigest()

    def _validarSenhaAtual(self, senha: str, cpf: str):
        senhaHash = self._calcularMd5(senha)
        return self.usuario_manager.getUserByCPF(cpf)[9] == senhaHash

    def alterarDadosUsuario(self, cpf:str, nome:str, sobrenome:str, nomeEmpresa:str, cargo:str, email:str, telefone:str, pais: str, senha:str, novaSenha: str, confirmeNovaSenha: str):
            if not Check.CPF(cpf):
                raise cpfInválido(cpf)
            if not Check.Nome(nome, sobrenome):
                raise nomeInválido(nome, sobrenome)
            if not Check.EMail(email):
                raise eMailInválido(email)
            if not Check.Telefone(telefone):
                raise telefoneInválido(telefone)
            if not Check.String(cargo):
                raise cargoInválido(cargo)
            if not Check.String(nomeEmpresa):
                raise nomeEmpresaInválido(nomeEmpresa)
            if not Check.String(pais):
                raise paisInválido(pais)
            if not Check.Senha(novaSenha, confirmeNovaSenha):
                raise senhaInválido()
            if not self._validarSenhaAtual(senha, cpf):
                raise senhaInválido()

            novaSenhaHash = self._calcularMd5(novaSenha)
            local_user['user'] = self.usuario_manager.alterarDadosUsuario(cpf,nome,sobrenome,nomeEmpresa,cargo,email,telefone,pais,novaSenhaHash)

            if config.DEBUG:
                print(local_user['user'][9])

            return True