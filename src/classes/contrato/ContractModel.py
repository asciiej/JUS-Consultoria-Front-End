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
            query = """
                INSERT INTO contracts.empresarial_contract (contratante, contratado, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
            params = (contract_dict['contratante'], contract_dict['contratado'], contract_dict['valor'], contract_dict['forma_pagamento'], contract_dict['multa_mora'], contract_dict['juros_mora'], contract_dict['correcao_monetaria'], contract_dict['prazo_duracao'])
            return self.db.query(query, params)
    
    def getEmpresarialContract(self):
        query = "SELECT * FROM contracts.empresarial_contract"
        return self.db.query(query)
    
    def getEmpresarialContractById(self, id:str):
        query = "SELECT * FROM contracts.empresarial_contract WHERE id = %s"
        result = self.db.query(query, (id,))
        if result:
            return result[0]
        return None
    
    def alterarDadosContratoEmpresarial(self, contract_id:int, contratante:str, contratado:str, valor:str, forma_pagamento:str, multa_mora:str, juros_mora:str, correcao_monetaria:str, prazo_duracao:str):
        contrato = self.getEmpresarialContractById(contract_id)
        if contrato:
            query = """
                UPDATE contracts.empresarial_contract
                SET contratante = %s,
                    contratado = %s,
                    valor = %s,
                    forma_pagamento = %s,
                    multa_mora = %s,
                    juros_mora = %s,
                    correcao_monetaria = %s,
                    prazo_duracao = %s
                WHERE id = %s
                """
            params = (contratante, contratado, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao, contrato[0])
            self.db.query(query, params)
        return self.getEmpresarialContract()
    
    def deleteEmpresarialContract(self, id:int):
        query = "DELETE FROM contracts.empresarial_contract WHERE id = %s"
        self.db.query(query, (id,))
        return self.getEmpresarialContract()
    