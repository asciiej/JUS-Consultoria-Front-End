class Contract:
    def __init__(self, contract_dict):
        self.nome_empresa = contract_dict['nome_empresa']
        self.cnpj = contract_dict['cnpj']
        self.cnae_principal = contract_dict['cnae_principal']
        self.cnae_secundario = contract_dict['cnae_secundario']
        self.cfop_principais = contract_dict['cfop_principais']
        self.industria_setor = contract_dict['industria_setor']
        self.receita_anual = contract_dict['receita_anual']

class ArbitragemContract(Contract):
    def __init__(self, contract_dict):
        super().__init__(contract_dict)

class TributariaContract(Contract):
    def __init__(self, contract_dict):
        super().__init__(contract_dict)

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
        # Add chamadas no DB aqui

    def create_tributaria_contract(self, contract_dict):
        tributaria = TributariaContract(contract_dict)

    def create_empresarial_contract(self, contract_dict):
        remuneracao = EmpresarialContract(contract_dict)

    def create_contract_model(self,tituloContrato : str,tipoContrato : str,textoContrato : list):
        query = f"INSERT INTO contractcontents.contract_model (tipo,titulo) values ('{tipoContrato}','{tituloContrato}') RETURNING id;"
        id = self.db.query(query)[0][0]
        for ordem,texto in textoContrato:
            query = f"INSERT INTO contractcontents.contract_text (text,ordem,contrato_referenciado) values ({texto},{ordem},{id});"
            self.db.query(query)
        print(id)
        print(tituloContrato,tipoContrato,textoContrato)

