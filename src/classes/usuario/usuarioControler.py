from  ...utilitarios.excecoes import *
import re
import hashlib
import validate_cpf

class UsuarioControler():
    def __init__(self, usuario_manager):
        self.usuario_manager = usuario_manager

    def login(self,eMail:str,senha:str):

        if not self._checkEMail(eMail):
            raise eMailInválido(eMail)

        if ' ' in senha:
            raise senhaInválido()

        senha = self._calcularMd5(senha)

        #Implementar a funcionalidade de login do crud]
        try:
            self.usuarioLogado = self.usuario_manager.login(eMail,senha)
        except Exception as e:
            print(e)
            return False
        print(self.usuarioLogado.str())
        return True
        #return (true or false) se o usuário for encontrado no banco ou não


    def cadastro(self,nome:str,sobrenome:str,cpf:str,nomeEmpresa:str,cargo:str,eMail:str,telefone:str,pais: str,senha:str,confirmeSenha:str):

        if not self._checkNome(nome,sobrenome):
            raise nomeInválido(nome,sobrenome)

        if not self._checkEMail(eMail):
           raise eMailInválido(eMail)

        # Telefones precisam ter código de país, código de area e o prefixo 9, indicando um telefone celular. Exemplo de telefone válido: cc (cc) c cccc-cccc
        if not self._checkTelefone(telefone):
            raise telefoneInválido(telefone)

        if not self._checkString(cargo):
            raise cargoInválido(cargo)

        if not self._checkString(nomeEmpresa):
            raise nomeEmpresaInválido(nomeEmpresa)

        if not self._checkString(pais):
            raise nomeEmpresaInválido(nomeEmpresa)

        if not self._checkSenha(senha,confirmeSenha):
            raise senhaInválido()

        # cpf obrigatóriamente no formato 111.111.111-11
        if not self._checkCPF(cpf):
            raise cpfInválido(cpf)

        senha = self._calcularMd5(senha) #converter a senha para hash md5 que será armazenado no banco de dados

        # aqui usamos as funcionalidades do model para inserir este usuário no banco de dados
        self.usuario_manager.cadastroUsuario(nome, sobrenome, cpf, nomeEmpresa, cargo, eMail, telefone, pais, senha)

    def _checkNome(self,nome:str,sobrenome:str):
        # Expressão regular para validar nomes com letras maiúsculas e minúsculas e acentos
        padraoNome = r'^[A-Za-zÀ-ÅÈ-ËÍ-ÏÐ-ÖØ-öø-ÿ]+$'

        # Expressão regular para validar nomes com letras maiúsculas e minúsculas, acentos e espaços
        padraoSobrenome = r'^[A-Za-zÀ-ÅÈ-ËÍ-ÏÐ-ÖØ-öø-ÿ\s]+$'

        if re.match(padraoNome, nome) and re.match(padraoSobrenome,sobrenome):
            return True
        else:
            return False

    def _checkEMail(self,eMail:str):
        # Expressão regular para verificar endereços de e-mail
        padraoEMail = r'^[\w\-.]+@(?:[a-zA-Z0-9]+\.)+[a-zA-Z]{2,}$'
        if re.match(padraoEMail, eMail):
            return True
        else:
            return False

    def _checkTelefone(self,telefone:str):
        padraoTelefone = r'^\+\d{2}\s\d{2}\s\d{5}-\d{4}$'

        if re.match(padraoTelefone, telefone):
            return True
        else:
            return False

    def _checkString(self,cargo:str):
        padraoCargo = r'^[A-Za-zÀ-ÅÈ-ËÍ-ÏÐ-ÖØ-öø-ÿ\s]+$'
        if re.match(padraoCargo, cargo):
            return True
        else:
            return False

    def _checkSenha(self,senha,confirmeSenha):
        return senha==confirmeSenha and ' ' not in senha

    def _checkCPF(self,cpf):
        padraoCPF = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        if re.match(padraoCPF, cpf) and validate_cpf.is_valid(cpf):
            return True
        else:
            return False

    def _calcularMd5(self,texto):
        # Codifica o texto em bytes antes de calcular o hash MD5
        texto_codificado = texto.encode('utf-8')

        # Calcula o hash MD5
        md5_hash = hashlib.md5(texto_codificado)

        # Retorna o hash MD5 como uma string hexadecimal
        return md5_hash.hexdigest()



#usuarioControler().cadastro("Lucas","Sabbatini Janot Procópio","lucas.exemplo@ufu.br","+55 12 34567-8901","Programador","ASCII","luc@s123","luc@s123")
