from ..ContractModel import TributariaContract

# =========================== Tributaria CRUD ===========================

def create_tributaria(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
    try:
        tributaria = TributariaContract(
            nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)
        query = """
            INSERT INTO
                contracts.tributaria_contract(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual;
            """
        params = (tributaria.nome_empresa, tributaria.cnpj, tributaria.cnae_principal, tributaria.cnae_secundario,
                  tributaria.cfop_principais, tributaria.industria_setor, tributaria.receita_anual)
        _query = self.db.query(query, params)
        if _query and len(_query) > 0:
            result = _query[0]
            return TributariaContract(id=result[0], nome_empresa=result[1], cnpj=result[2], cnae_principal=result[3], cnae_secundario=result[4], cfop_principais=result[5], industria_setor=result[6], receita_anual=result[7])
    except Exception as e:
        print(f"Erro ao criar contrato tributário: {str(e)}")
        return None


def get_tributaria_by_id(self, id: str):
    try:
        query = "SELECT * FROM contracts.tributaria_contract WHERE id = %s"
        _query = self.db.query(query, (id,))
        if _query and len(_query) > 0:
            result = _query[0]
            return TributariaContract(id=result[0], nome_empresa=result[1], cnpj=result[2], cnae_principal=result[3], cnae_secundario=result[4], cfop_principais=result[5], industria_setor=result[6], receita_anual=result[7])
    except Exception as e:
        print(f"Erro ao buscar contrato tributário por ID {id}: {str(e)}")
    return None


def get_all_tributaria(self):
    try:
        query = "SELECT * FROM contracts.tributaria_contract"
        _query = self.db.query(query)
        if _query and len(_query) > 0:
            return [
                TributariaContract(
                    id=row[0], nome_empresa=row[1], cnpj=row[2], cnae_principal=row[3],
                    cnae_secundario=row[4], cfop_principais=row[5], industria_setor=row[6],
                    receita_anual=row[7]
                ) for row in _query
            ]
    except Exception as e:
        print(f"Erro ao buscar todos os contratos tributários: {str(e)}")
    return []


def update_tributaria(self, id_contrato: str, nomeEmpresa: str, cnpj: str, cnaePrincipal: str, cnaeSecundaria: str, cfopPrincipais: str, industriaSetor: str, receitaAnual: float):
    try:
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
                RETURNING id, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual;
                """
            params = (nomeEmpresa, cnpj, cnaePrincipal, cnaeSecundaria,
                      cfopPrincipais, industriaSetor, receitaAnual, id_contrato)
            _query = self.db.query(query, params)
            if _query and len(_query) > 0:
                result = _query[0]
                return TributariaContract(id=result[0], nome_empresa=result[1], cnpj=result[2], cnae_principal=result[3], cnae_secundario=result[4], cfop_principais=result[5], industria_setor=result[6], receita_anual=result[7])
    except Exception as e:
        print(f"Erro ao atualizar contrato tributário com ID {id_contrato}: {str(e)}")
    return None


def delete_tributaria(self, contract_id):
    try:
        query = "DELETE FROM contracts.tributaria_contract WHERE id = %s"
        self.db.query(query, (contract_id,))
        return self.get_all_tributaria()
    except Exception as e:
        print(f"Erro ao deletar contrato tributário com ID {contract_id}: {str(e)}")
        return []
