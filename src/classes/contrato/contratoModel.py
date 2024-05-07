import usuario.usuarioModel as usuario
class contratoModel:
  
    def init(self,titulo:str,tipo:str):
        self.titulo = titulo
        self.tipo = tipo
        

    def str(self)->str:
         return (f"Titulo: {self.titulo}\n"
                f"Tipo: {self.tipo}")
    

class campoDeUmContrato:

    def init(self,tipo:str,texto:str):
        self.tipo = tipo
        self.texto = texto

    def str(self)->str:
        return(f"Texto: {self.texto}")


class parteDeUmContrato:
    def init(self,nomeCompleto:str,nacionalidade:str,estadoCivil:str,profissao:str,cpf:str,cnjp:str,endereco:str):
        self.nomeCompleto = nomeCompleto
        self.nacionalidade = nacionalidade
        self.estadoCivil = estadoCivil
        self.profissao = profissao
        self.cpf = cpf
        self.cnpj = cnjp
        self.endereco = endereco

    def str(self)->str:
         return (f"NomeCompleto: {self.nomeCompleto}\n"
                f"Nacionalidade: {self.nacionalidade}\n"
                f"EstadoCivil: {self.estadoCivil}\n"
                f"Profissao: {self.profissao}\n"
                f"CPF: {self.cpf}\n"
                f"CNPJ: {self.cnpj}\n"
                f"Endereco: {self.endereco}")


class contratoIndividualModel (contratoModel): 

    def init(self,titulo:str,tipo:str,valor:str,formaDePagamento:str,multaEncargos:str,prazoDuracao:str,usuario:usuario,camposDeUmContrato:list,partesDeUmContrato:list):
        super().init(titulo,tipo)
        self.valor = valor
        self.formaDePagamento = formaDePagamento
        self.multaEncargos = multaEncargos
        self.prazoDuracao = prazoDuracao
        self.usuario = usuario
        self.camposDeUmcontrato = camposDeUmContrato
        self.partesDeUmContrato = partesDeUmContrato

    def str(self) ->str:
        return (f"Usuario: {self.usuario.nome}\n" 
                f"Valor: {self.valor}\n"
                f"FormaDePagamento: {self.formaDePagamento}\n"
                f"MultaEncargos: {self.multaEncargos}\n"
                f"PrazoDuracao: {self.prazoDuracao}\n")

    
