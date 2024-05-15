# import usuario.usuarioModel as usuario
# class contratoModel:
  
#     def init(self,titulo:str,tipo:str):
#         self.titulo = titulo
#         self.tipo = tipo
        

#     def str(self)->str:
#          return (f"Titulo: {self.titulo}\n"
#                 f"Tipo: {self.tipo}")
    

# class campoDeUmContrato:

#     def init(self,tipo:str,texto:str):
#         self.tipo = tipo
#         self.texto = texto

#     def str(self)->str:
#         return(f"Texto: {self.texto}")


# class parteDeUmContrato:
#     def init(self,nomeCompleto:str,nacionalidade:str,estadoCivil:str,profissao:str,cpf:str,cnjp:str,endereco:str):
#         self.nomeCompleto = nomeCompleto
#         self.nacionalidade = nacionalidade
#         self.estadoCivil = estadoCivil
#         self.profissao = profissao
#         self.cpf = cpf
#         self.cnpj = cnjp
#         self.endereco = endereco

#     def str(self)->str:
#          return (f"NomeCompleto: {self.nomeCompleto}\n"
#                 f"Nacionalidade: {self.nacionalidade}\n"
#                 f"EstadoCivil: {self.estadoCivil}\n"
#                 f"Profissao: {self.profissao}\n"
#                 f"CPF: {self.cpf}\n"
#                 f"CNPJ: {self.cnpj}\n"
#                 f"Endereco: {self.endereco}")


# class contratoIndividualModel (contratoModel): 

#     def init(self,titulo:str,tipo:str,valor:str,formaDePagamento:str,multaEncargos:str,prazoDuracao:str,usuario:usuario,camposDeUmContrato:list,partesDeUmContrato:list):
#         super().init(titulo,tipo)
#         self.valor = valor
#         self.formaDePagamento = formaDePagamento
#         self.multaEncargos = multaEncargos
#         self.prazoDuracao = prazoDuracao
#         self.usuario = usuario
#         self.camposDeUmcontrato = camposDeUmContrato
#         self.partesDeUmContrato = partesDeUmContrato

#     def str(self) ->str:
#         return (f"Usuario: {self.usuario.nome}\n" 
#                 f"Valor: {self.valor}\n"
#                 f"FormaDePagamento: {self.formaDePagamento}\n"
#                 f"MultaEncargos: {self.multaEncargos}\n"
#                 f"PrazoDuracao: {self.prazoDuracao}\n")
class Contract:
    def __init__(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.cnae_principal = cnae_principal
        self.cnae_secundario = cnae_secundario
        self.cfop_principais = cfop_principais
        self.industria_setor = industria_setor
        self.receita_anual = receita_anual

class ConsultoriaTributariaContract(Contract):
    def __init__(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        super().__init__(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)

class ArbitragemContract(Contract):
    def __init__(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        super().__init__(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)

class ConsultoriaEmpresarialContract(Contract):
    def __init__(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual,
                 partes, objeto_contrato, forma_condicoes_remuneracao, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao):
        super().__init__(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)
        self.partes = partes
        self.objeto_contrato = objeto_contrato
        self.forma_condicoes_remuneracao = forma_condicoes_remuneracao
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.multa_mora = multa_mora
        self.juros_mora = juros_mora
        self.correcao_monetaria = correcao_monetaria
        self.prazo_duracao = prazo_duracao

class ContractManager:
    def __init__(self):
        self.contracts = []

    def create_contract(self, contract):
        self.contracts.append(contract)

    def read_contract(self, nome_empresa):
        for contract in self.contracts:
            if contract.nome_empresa == nome_empresa:
                return contract
        return None

    def update_contract(self, nome_empresa, new_contract_data):
        for contract in self.contracts:
            if contract.nome_empresa == nome_empresa:
                # Atualiza os campos do contrato com os novos dados
                for key, value in new_contract_data.items():
                    setattr(contract, key, value)
                return True
        return False

    def delete_contract(self, nome_empresa):
        for contract in self.contracts:
            if contract.nome_empresa == nome_empresa:
                self.contracts.remove(contract)
                return True
        return False

# Exemplo de uso:

# Criar uma instância do gerenciador de contratos
contract_manager = ContractManager()

# Criar um novo contrato
new_contract = Contract(nome_empresa="Empresa A", cnpj="123456789", cnae_principal="1234", cnae_secundario="5678", cfop_principais="9012", industria_setor="Indústria", receita_anual=1000000)
contract_manager.create_contract(new_contract)

# Ler um contrato pelo nome da empresa
contract = contract_manager.read_contract("Empresa A")
print("Contrato encontrado:", contract.nome_empresa)

# Atualizar um contrato
updated_data = {"cnae_principal": "4321", "receita_anual": 2000000}
contract_manager.update_contract("Empresa A", updated_data)
updated_contract = contract_manager.read_contract("Empresa A")
print("CNAE Principal atualizado:", updated_contract.cnae_principal)

# Deletar um contrato
contract_manager.delete_contract("Empresa A")
deleted_contract = contract_manager.read_contract("Empresa A")
print("Contrato deletado:", deleted_contract)