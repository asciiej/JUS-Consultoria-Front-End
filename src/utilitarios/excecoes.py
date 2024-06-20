
class NomeInvalido(Exception):
    def __init__(self, nome,sobrenome):
        self.mensagem = f'Nome: {nome} ou Sobrenome: {sobrenome} inválidos'
        super().__init__(self.mensagem)

class EmailInvalido(Exception):
    def __init__(self, eMail):
        self.mensagem = f'E-Mail: {eMail} inválido'
        super().__init__(self.mensagem)

class TelefoneInvalido(Exception):
    def __init__(self, telefone):
        self.mensagem = f'Telefone: {telefone} inválido'
        super().__init__(self.mensagem)

class CargoInvalido(Exception):
    def __init__(self, cargo):
        self.mensagem = f'Cargo: {cargo} inválido'
        super().__init__(self.mensagem)

class NomeEmpresaInvalido(Exception):
    def __init__(self, nomeEmpresa):
        self.mensagem = f'Nome da Empresa: {nomeEmpresa} inválido'
        super().__init__(self.mensagem)

class SenhaInvalido(Exception):
    def __init__(self):
        self.mensagem = f'Senhas inválidas ou diferentes'
        super().__init__(self.mensagem)

class PaisInvalido(Exception):
    def __init__(self, pais):
        self.mensagem = f'País: {pais} inválido'
        super().__init__(self.mensagem)

class CPFInvalido(Exception):
    def __init__(self,cpf):
        self.mensagem = f'CPF: {cpf} inválido'
        super().__init__(self.mensagem)

class UsuarioOuSenhaInvalido(Exception):
    def __init__(self):
        self.mensagem = 'Usuário ou Senha Inválidos'
        super().__init__(self.mensagem)
