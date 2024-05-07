class usuarioModel: 
    def init(self, nome: str, sobrenome: str, email: str, telefone: str, pais: str, cargo: str = None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone
        self.pais = pais
        self.cargo = cargo

    def str(self) -> str:
        return (f"Nome: {self.nome} {self.sobrenome}\n"
                f"Cargo: {self.cargo if self.cargo is not None else 'Não informado'}\n"
                f"E-mail: {self.email}\n"
                f"Telefone: {self.telefone}\n"
                f"País/Localização: {self.pais}")