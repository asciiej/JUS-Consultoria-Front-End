import config

class Contract:
    def __init__(self, id, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        self.id = id
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.cnae_principal = cnae_principal
        self.cnae_secundario = cnae_secundario
        self.cfop_principais = cfop_principais
        self.industria_setor = industria_setor
        self.receita_anual = receita_anual

    def str(self):
        return (
            f"""
            Contrato:
            ID: {self.id} -
            Nome: {self.nome_empresa} -
            CNPJ: {self.cnpj} -
            CNAE: {self.cnae_principal} -
            CNAE: {self.cnae_secundario} -
            CFOP: {self.cfop_principais} -
            Setor: {self.industria_setor} -
            Receita: {self.receita_anual}"""
        )

class ArbitragemContract(Contract):
    def __init__(self, id, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        super().__init__(id, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)

class TributariaContract(Contract):
    def __init__(self, id, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        super().__init__(id, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)

class EmpresarialContract:
    def __init__(self, id, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao, contratante_id, contratado_id):
        self.id = id
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.multa_mora = multa_mora
        self.juros_mora = juros_mora
        self.correcao_monetaria = correcao_monetaria
        self.prazo_duracao = prazo_duracao
        self.contratante_id = contratante_id
        self.contratado_id = contratado_id

    def str(self):
        return (
            f"""
            Contrato:
            ID: {self.id} -
            Valor: {self.valor} -
            Forma de Pagamento: {self.forma_pagamento} -
            Multa Mora: {self.multa_mora} -
            Juros Mora: {self.juros_mora} -
            Correção Monetaria: {self.correcao_monetaria} -
            Prazo Duração: {self.prazo_duracao} -
            Contratante ID: {self.contratante_id} -
            Contratado ID: {self.contratado_id}"""
        )

class EmpresarialPerson:
    def __init__(self, id, nome, nacionalidade, estadocivil, cpf, profissao, endereco):
        self.id = id
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.estadocivil = estadocivil
        self.cpf = cpf
        self.profissao = profissao
        self.endereco = endereco

class ContractManager:
    def __init__(self, db):
        self.db = db

    from .contracts.Arbitragem import (
        create_arbitragem, delete_arbitragem, get_all_arbitragem, get_arbitragem_by_id, update_arbitragem
    )

    from .contracts.Tributaria import (
       create_tributaria, delete_tributaria, get_all_tributaria, get_tributaria_by_id, update_tributaria
    )

    from .contracts.Empresarial import (
        create_empresarial_contract,
        get_all_empresarial,
        get_empresarial_by_id,
        update_empresarial,
        delete_empresarial_contract,

        create_contratado,
        get_all_contratado,
        update_contratado,
        delete_contratado,
        get_contratado_by_id,

        create_contratante,
        get_all_contratante,
        update_contratante,
        delete_contratante,
        get_contratante_by_id,
    )

    # =========================== Model CRUD ===========================

    def create_contract_model(self,tituloContrato : str,tipoContrato : str,textoContrato : list):
        query = f"INSERT INTO contractcontents.contract_model (tipo,titulo) values ('{tipoContrato}','{tituloContrato}') RETURNING id;"
        id = self.db.query(query)[0][0]
        for ordem,texto in textoContrato:
            query = f"INSERT INTO contractcontents.contract_text (text,ordem,contrato_referenciado) values ('{texto}',{ordem},{id});"
            retorno = self.db.query(query)
        if config.DEBUG:
            print(retorno)

    def update_contract_model(self,tituloContrato:str,textoContrato:list):
        id = self.get_id_contract_modelByTitle(tituloContrato)
        query = f"DELETE FROM contractcontents.contract_text WHERE contrato_referenciado = {id};"
        self.db.query(query)
        for ordem,texto in textoContrato:
            query = f"INSERT INTO contractcontents.contract_text (text,ordem,contrato_referenciado) values ('{texto}',{ordem},{id});"
            retorno = self.db.query(query)
        if config.DEBUG:
            print(retorno)
        
    def get_contract_model_byId(self,id: int):
        query = f"SELECT * FROM contractcontents.contract_text WHERE contrato_referenciado = {id};"
        return self.db.query(query)

    def get_contract_model_byTitle(self,title):
        id = self.get_id_contract_modelByTitle(title)
        query = f"SELECT * FROM contractcontents.contract_text WHERE contrato_referenciado = {id};"
        return self.db.query(query)
    
    def get_id_contract_modelByTitle(self,title):
        query = f"SELECT id FROM contractcontents.contract_model WHERE titulo = '{title}';"
        id = self.db.query(query)[0][0]
        return id