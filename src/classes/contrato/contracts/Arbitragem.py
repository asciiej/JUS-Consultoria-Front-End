from ..ContractModel import ArbitragemContract

# =========================== Arbitragem CRUD ===========================


def create_arbitragem(self, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual):
    try:
        query = """
						INSERT INTO
								contracts.arbitragem_contract(nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual)
						VALUES (%s, %s, %s, %s, %s, %s, %s)
						RETURNING id, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual;
						"""
        params = (nome_empresa, cnpj, cnae_principal, cnae_secundario,
                  cfop_principais, industria_setor, receita_anual)
        _query = self.db.query(query, params)
        if _query and len(_query) > 0:
            result = _query[0]
            return ArbitragemContract(id=result[0], nome_empresa=result[1], cnpj=result[2], cnae_principal=result[3], cnae_secundario=result[4], cfop_principais=result[5], industria_setor=result[6], receita_anual=result[7])
    except Exception as e:
        print(f"Erro ao criar contrato de arbitragem: {str(e)}")
        return None

# Função para obter um contrato de arbitragem pelo ID


def get_arbitragem_by_id(self, id: str):
    try:
        query = "SELECT * FROM contracts.arbitragem_contract WHERE id = %s"
        _query = self.db.query(query, (id,))
        if _query and len(_query) > 0:
            result = _query[0]
            return ArbitragemContract(id=result[0], nome_empresa=result[1], cnpj=result[2], cnae_principal=result[3], cnae_secundario=result[4], cfop_principais=result[5], industria_setor=result[6], receita_anual=result[7])
    except Exception as e:
        print(f"Erro ao buscar contrato de arbitragem por ID {id}: {str(e)}")
    return None

# Função para obter todos os contratos de arbitragem


def get_all_arbitragem(self):
    try:
        query = "SELECT * FROM contracts.arbitragem_contract"
        _query = self.db.query(query)
        if _query and len(_query) > 0:
            result = _query[0]
            return [
                ArbitragemContract(
                    id=row[0], nome_empresa=row[1], cnpj=row[2], cnae_principal=row[3],
                    cnae_secundario=row[4], cfop_principais=row[5], industria_setor=row[6],
                    receita_anual=row[7]
                ) for row in result
            ]
    except Exception as e:
        print(f"Erro ao buscar todos os contratos de arbitragem: {str(e)}")
        return []
    return []

# Função para atualizar um contrato de arbitragem existente


def update_arbitragem(self, id_contrato: str, nomeEmpresa: str, cnpj: str, cnaePrincipal: str, cnaeSecundaria: str, cfopPrincipais: str, industriaSetor: str, receitaAnual: float):
    try:
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
								RETURNING id, nome_empresa, cnpj, cnae_principal, cnae_secundario, cfop_principais, industria_setor, receita_anual
								"""
            params = (nomeEmpresa, cnpj, cnaePrincipal, cnaeSecundaria,
                      cfopPrincipais, industriaSetor, receitaAnual, id_contrato)
            _query = self.db.query(query, params)
            if _query and len(_query) > 0:
                result = _query[0]
                return ArbitragemContract(id=result[0], nome_empresa=result[1], cnpj=result[2], cnae_principal=result[3], cnae_secundario=result[4], cfop_principais=result[5], industria_setor=result[6], receita_anual=result[7])
    except Exception as e:
        print(f"Erro ao atualizar contrato de arbitragem com ID {id_contrato}: {str(e)}")
    return None

# Função para deletar um contrato de arbitragem pelo ID


def delete_arbitragem(self, contract_id):
    try:
        query = "DELETE FROM contracts.arbitragem_contract WHERE id = %s"
        self.db.query(query, (contract_id,))
    except Exception as e:
        print(f"Erro ao deletar contrato de arbitragem com ID {contract_id}: {str(e)}")
        return []
