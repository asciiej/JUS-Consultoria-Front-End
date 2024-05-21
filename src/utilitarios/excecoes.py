
class nomeInválido(Exception):
    def __init__(self, nome,sobrenome):
        self.mensagem = f'Nome: {nome} ou Sobrenome: {sobrenome} inválidos'
        super().__init__(self.mensagem)

class eMailInválido(Exception):
    def __init__(self, eMail):
        self.mensagem = f'E-Mail: {eMail} inválido'
        super().__init__(self.mensagem)

class telefoneInválido(Exception):
    def __init__(self, telefone):
        self.mensagem = f'Telefone: {telefone} inválido'
        super().__init__(self.mensagem)

class cargoInválido(Exception):
    def __init__(self, cargo):
        self.mensagem = f'Cargo: {cargo} inválido'
        super().__init__(self.mensagem)

class nomeEmpresaInválido(Exception):
    def __init__(self, nomeEmpresa):
        self.mensagem = f'Nome da Empresa: {nomeEmpresa} inválido'
        super().__init__(self.mensagem)

class senhaInválido(Exception):
    def __init__(self):
        self.mensagem = f'Senhas inválidas ou diferentes'
        super().__init__(self.mensagem)

class paisInválido(Exception):
    def __init__(self, pais):
        self.mensagem = f'País: {pais} inválido'
        super().__init__(self.mensagem)

class cpfInválido(Exception):
    def __init__(self,cpf):
        self.mensagem = f'CPF: {cpf} inválido'
        super().__init__(self.mensagem)

class usuarioOuSenhaInválido(Exception):
    def __init__(self):
        self.mensagem = 'Usuário ou Senha Inválidos'
        super().__init__(self.mensagem)
