#Nome ou sobrenome inválido
#eMail Inválido
#Telefone Inválido
#Cargo Inválido
#Empresa Inválido
#Senhas inválidas ou diferentes


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
    def __init__(self, senha):
        self.mensagem = f'Senhas inválidas ou diferentes'
        super().__init__(self.mensagem)