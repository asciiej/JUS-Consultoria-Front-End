import config

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
    def __init__(self, contratante, contratado, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao):
        self.contratante = contratante
        self.contratado = contratado
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.multa_mora = multa_mora
        self.juros_mora = juros_mora
        self.correcao_monetaria = correcao_monetaria
        self.prazo_duracao = prazo_duracao

class ContractManager:
    def __init__(self, db):
        self.db = db

    # ============================ Arbitragem CRUD ============================
    def create_arbitragem(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        arbitragem = ArbitragemContract(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)
        # Add chamadas no DB aqui

    # ============================ Tributaria CRUD ============================

    def create_tributaria(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        tributaria = TributariaContract(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)
        query = """
                INSERT INTO
                    contracts.tributaria_contract(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
        params = (nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)
        return self.db.query(query, params)

    def get_tributaria_by_id(self, id: str):
        query = "SELECT * FROM  contracts.tributaria_contract WHERE id = %s"
        result = self.db.query(query, (id,))
        if result:
            return result[0]
        return None

    def get_all_tributaria(self):
        query = "SELECT * FROM contracts.tributaria_contract"
        return self.db.query(query)

    def update_tributaria(self, id_contrato: str, nomeEmpresa: str, cnpj: str, cnaePrincipal: str, cnaeSecundaria: str, cfopPrincipais: str, industriaSetor: str, receitaAnual: float):
        contrato = self.get_tributaria_by_id(id_contrato)
        if contrato:
            query = """
                UPDATE contracts.tributaria_contract
                SET nome_empresa = %s,
                    cnpj = %s,
                    cnae_principal = %s,
                    cnae_secundario = %s,
                    cfop_principais = %s,
                    industria_setor = %s,
                    receita_anual = %s
                WHERE id = %s
                """
            params = (nomeEmpresa, cnpj, cnaePrincipal, cnaeSecundaria, cfopPrincipais, industriaSetor, receitaAnual, id_contrato)
            self.db.query(query, params)
        return self.get_tributaria_by_id(id_contrato)

    def delete_tributaria(self, contract_id):
        query = "DELETE FROM contracts.tributaria_contract WHERE id = %s"
        self.db.query(query, (contract_id,))
        return self.get_all_tributaria()

    # ============================ Model CRUD ============================

    def create_contract_model(self,tituloContrato : str,tipoContrato : str,textoContrato : list):
        query = f"INSERT INTO contractcontents.contract_model (tipo,titulo) values ('{tipoContrato}','{tituloContrato}') RETURNING id;"
        id = self.db.query(query)[0][0]
        for ordem,texto in textoContrato:
            query = f"INSERT INTO contractcontents.contract_text (text,ordem,contrato_referenciado) values ('{texto}',{ordem},{id});"
            retorno = self.db.query(query)
        if config.DEBUG:
            print(retorno)

    def get_contract_model(self,id: int):
        query = f"SELECT * FROM contractcontents.contract_text WHERE contrato_referenciado = {id};"
        return self.db.query(query)



    # ============================ Empresarial CRUD ============================

    def create_empresarial_contract(self, contratante, contratado, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao):
            query = """
                INSERT INTO contracts.empresarial_contract (contratante, contratado, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
            params = (contratante, contratado, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao)
            return self.db.query(query, params)

    def get_all_empresarial(self):
        query = "SELECT * FROM contracts.empresarial_contract"
        return self.db.query(query)

    def get_empresarial_by_id(self, id:str):
        query = "SELECT * FROM contracts.empresarial_contract WHERE id = %s"
        result = self.db.query(query, (id,))
        if result:
            return result[0]
        return None

    def update_empresarial(self, contract_id:int, contratante:str, contratado:str, valor:str, forma_pagamento:str, multa_mora:str, juros_mora:str, correcao_monetaria:str, prazo_duracao:str):
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

    def delete_empresarial_contract(self, id:int):
        query = "DELETE FROM contracts.empresarial_contract WHERE id = %s"
        self.db.query(query, (id,))
        return self.getEmpresarialContract()
