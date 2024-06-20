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
        query = """
                INSERT INTO
                    contracts.arbitragem_contract(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual;
                """
        params =  (arbitragem.nome_empresa, arbitragem.cnpj, arbitragem.cnae_principal, arbitragem.cnae_secundario, arbitragem.cfop_principais, arbitragem.industria_setor, arbitragem.receita_anual)
        resultDB = self.db.query(query, params)
        if resultDB and len(resultDB) > 0:
            result = resultDB[0]
            return ArbitragemContract(nome_empresa=result[1], cnpj=result[2], cnae_principal=result[3], cnae_secundario=result[4], cfop_principais=result[5], industria_setor=result[6], receita_anual=result[7])

    def get_arbitragem_by_id(self, id: str):
        query = "SELECT * FROM  contracts.arbitragem_contract WHERE id = %s"
        resultDB = self.db.query(query, (id,))
        if resultDB and len(resultDB) > 0:
            result = resultDB[0]
            return ArbitragemContract(nome_empresa=result[1], cnpj=result[2], cnae_principal=result[3], cnae_secundario=result[4], cfop_principais=result[5], industria_setor=result[6], receita_anual=result[7])
        return None

    def get_all_arbitragem(self):
        query = "SELECT * FROM contracts.arbitragem_contract"
        return self.db.query(query)

    def update_arbitragem(self, id_contrato: str, nomeEmpresa: str, cnpj: str, cnaePrincipal: str, cnaeSecundaria: str, cfopPrincipais: str, industriaSetor: str, receitaAnual: float):
        contrato = self.get_arbitragem_by_id(id_contrato)
        if contrato:
            query = """
                UPDATE contracts.arbitragem_contract
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
        return self.get_arbitragem_by_id(id_contrato)

    def delete_arbitragem(self, contract_id):
        query = "DELETE FROM contracts.arbitragem_contract WHERE id = %s"
        self.db.query(query, (contract_id,))
        return self.get_all_arbitragem()
    # ============================ Tributaria CRUD ============================

    def create_tributaria(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
        tributaria = TributariaContract(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)
        query = """
                INSERT INTO
                    contracts.tributaria_contract(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual;
                """
        params =  (tributaria.nome_empresa, tributaria.cnpj, tributaria.cnae_principal, tributaria.cnae_secundario, tributaria.cfop_principais, tributaria.industria_setor, tributaria.receita_anual)
        resultDB = self.db.query(query, params)
        if resultDB and len(resultDB) > 0:
            result = resultDB[0]
            return TributariaContract(nome_empresa=result[1], cnpj=result[2], cnae_principal=result[3], cnae_secundario=result[4], cfop_principais=result[5], industria_setor=result[6], receita_anual=result[7])

    def get_tributaria_by_id(self, id: str):
        query = "SELECT * FROM  contracts.tributaria_contract WHERE id = %s"
        resultDB = self.db.query(query, (id,))
        if resultDB and len(resultDB) > 0:
            result = resultDB[0]
            return TributariaContract(nome_empresa=result[1], cnpj=result[2], cnae_principal=result[3], cnae_secundario=result[4], cfop_principais=result[5], industria_setor=result[6], receita_anual=result[7])
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

    def get_contract_model_byId(self,id: int):
        query = f"SELECT * FROM contractcontents.contract_text WHERE contrato_referenciado = {id};"
        return self.db.query(query)

    def get_contract_model_byTitle(self,title):
        query = f"SELECT id FROM contractcontents.contract_model WHERE titulo = '{title}';"

        id = self.db.query(query)[0][0]
        query = f"SELECT * FROM contractcontents.contract_text WHERE contrato_referenciado = {id};"
        return self.db.query(query)

    def udate_contract_model(self,id):
        pass

    # ============================ CONTRATADO CRUD ============================

    def create_contratado(self, nome: str, nacionalidade: str, estadocivil: str, cpf: str, profissao: str, endereco: str):
        query = """
            INSERT INTO contracts.contratada (nome, nacionalidade, estadocivil, cpf, profissao, endereco)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
        """
        params = (nome, nacionalidade, estadocivil, cpf, profissao, endereco)
        result = self.db.query(query, params)
        return result[0]['id']

    def get_all_contratado(self):
        query = "SELECT * FROM contracts.contratada"
        return self.db.query(query)

    def update_contratado(self, nome: str, nacionalidade: str, estadocivil: str, cpf: str, profissao: str, endereco: str):
        query = """
            UPDATE contracts.contratada
            SET nome = %s, nacionalidade = %s, estadocivil = %s, cpf = %s, profissao = %s, endereco = %s
            WHERE id = %s RETURNING id
        """
        params = (nome, nacionalidade, estadocivil, cpf, profissao, endereco)
        result = self.db.query(query, params)
        return result[0]['id']


    def delete_contratado(self, id:int):
        query = "DELETE FROM contracts.contratada WHERE id = %s"
        self.db.query(query, (id,))
        return self.getContratado()

    def get_contratado_by_id(self, id:str):
        query = "SELECT * FROM contracts.contratada WHERE id = %s"
        result = self.db.query(query, (id,))
        if result:
            return result[0]
        return None




    # ============================ CONTRATANTE CRUD ============================

    def create_contratante(self, nome: str, nacionalidade: str, estadocivil: str, cpf: str, profissao: str, endereco: str):
        query = """
            INSERT INTO contracts.contratante (nome, nacionalidade, estadocivil, cpf, profissao, endereco)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
        """
        params = (nome, nacionalidade, estadocivil, cpf, profissao, endereco)
        result = self.db.query(query, params)
        return result[0]['id']

    def get_contratante_by_id(self, id:str):
        query = "SELECT * FROM contracts.contratante WHERE id = %s"
        result = self.db.query(query, (id,))
        if result:
            return result[0]
        return None

    def get_all_contratante(self):
        query = "SELECT * FROM contracts.contratante"
        return self.db.query(query)

    def update_contratante(self, nome: str, nacionalidade: str, estadocivil: str, cpf: str, profissao: str, endereco: str):
        query = """
            UPDATE contracts.contratante
            SET nome = %s, nacionalidade = %s, estadocivil = %s, cpf = %s, profissao = %s, endereco = %s
            WHERE id = %s RETURNING id
        """
        params = (nome, nacionalidade, estadocivil, cpf, profissao, endereco)
        result = self.db.query(query, params)
        return result[0]['id']

    def delete_contratante(self, id:int):
        query = "DELETE FROM contracts.contratante WHERE id = %s"
        self.db.query(query, (id,))
        return self.getContratado()

    # ============================ EMPRESARIAL CRUD ============================

    def create_empresarial_contract(self, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao, contratante_id, contratado_id):
        query = """
                INSERT INTO contracts.empresarial_contract (valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao, contratante_id, contratado_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
        params = (valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao, contratante_id, contratado_id)
        resultDB = self.db.query(query, params)
        if resultDB and len(resultDB) > 0:
            result = resultDB[0]
            return EmpresarialContract(contratante=result[1], contratado=result[2], valor=result[3], forma_pagamento=result[4], multa_mora=result[5], juros_mora=result[6], correcao_monetaria=result[7], prazo_duracao=result[8])

    def get_all_empresarial(self):
        query = "SELECT * FROM contracts.empresarial_contract"
        return self.db.query(query)

    def get_empresarial_by_id(self, id:str):
        query = "SELECT * FROM contracts.empresarial_contract WHERE id = %s"
        result = self.db.query(query, (id,))
        if result:
            return result[0]
        return None

    def update_empresarial(self, contract_id:int, contratante:str, contratado:str, valor:str, forma_pagamento:str, multa_mora:str, juros_mora:str, correcao_monetaria:str, prazo_duracao:str, contract_dict):
        contrato = self.getEmpresarialContractById(contract_id)
        contratante_id = self.update_contratante(contract_dict['contratante'])
        contratado_id = self.update_contratado(contract_dict['contratado'])

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
            params = (contratante_id, contratado_id, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao, contrato[0])
            self.db.query(query, params)
        return self.get_empresarial_by_id(contract_id)

    def delete_empresarial_contract(self, id:int):
        query = "DELETE FROM contracts.empresarial_contract WHERE id = %s"
        self.db.query(query, (id,))
        return self.getEmpresarialContract()

    # ============================ CRUD============================
