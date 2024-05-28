class Contract:
    def __init__(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.cnae_principal = cnae_principal
        self.cnae_secundario = cnae_secundario
        self.cfop_principais = cfop_principais
        self.industria_setor = industria_setor
        self.receita_anual = receita_anual

class ArbitragemContract(Contract):
    def __init__(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        super().__init__(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)

class TributariaContract(Contract):
    def __init__(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        super().__init__(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)

class EmpresarialContract:
    def __init__(self, contract_dict):
        self.contratante = contract_dict['contratante']
        self.contratado = contract_dict['contratado']
        self.valor = contract_dict['valor']
        self.forma_pagamento = contract_dict['forma_pagamento']
        self.multa_mora = contract_dict['multa_mora']
        self.juros_mora = contract_dict['juros_mora']
        self.correcao_monetaria = contract_dict['correcao_monetaria']
        self.prazo_duracao = contract_dict['prazo_duracao']

class ContractManager:
    def __init__(self, db):
        self.db = db

    def create_arbitragem_contract(self, contract_dict):
        arbitragem = ArbitragemContract(contract_dict)

    def create_tributaria_contract(self, contract_dict):
        tributaria = TributariaContract(contract_dict)

    def create_empresarial_contract(self, contract_dict):
        remuneracao = EmpresarialContract(contract_dict)
        self.db.query("""SELECT * FROM contract""")
        print(remuneracao.contratado)
