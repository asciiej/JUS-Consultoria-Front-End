from ..ContractModel import EmpresarialContract, EmpresarialPerson


def create_empresarial_contract(self, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao, contratante_id, contratado_id):
    try:
        query = """
            INSERT INTO contracts.empresarial_contract (
                valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria,
                prazo_duracao, contratante_id, contratado_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao, contratante_id, contratado_id
        """
        params = (valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao, contratante_id, contratado_id)
        _query = self.db.query(query, params)
        if _query and len(_query) > 0:
            result = _query[0]
            return EmpresarialContract(
                id=result[0],
                valor=result[1],
                forma_pagamento=result[2],
                multa_mora=result[3],
                juros_mora=result[4],
                correcao_monetaria=result[5],
                prazo_duracao=result[6],
                contratante_id=result[7],
                contratado_id=result[8]
            )
    except Exception as e:
        print(f"Erro ao criar o contrato empresarial: {str(e)}")
    return None

def get_all_empresarial(self):
    try:
        query = "SELECT * FROM contracts.empresarial_contract"
        _query = self.db.query(query)

        if not _query:
            raise Exception('Nenhum contrato empresarial encontrado')

        return [
            EmpresarialContract(
                id=row[0],  # Incluindo o ID
                valor=row[1],
                forma_pagamento=row[2],
                multa_mora=row[3],
                juros_mora=row[4],
                correcao_monetaria=row[5],
                prazo_duracao=row[6],
                contratante_id=row[7],
                contratado_id=row[8]
            ) for row in _query
        ]
    except Exception as e:
        print(f"Erro ao buscar todos os contratos empresariais: {str(e)}")
    return []

def get_empresarial_by_id(self, id: int):
    try:
        query = "SELECT * FROM contracts.empresarial_contract WHERE id = %s"
        _query = self.db.query(query, (id,))
        if _query and len(_query) > 0:
            result = _query[0]
            return EmpresarialContract(
                id=result[0],  # Incluindo o ID
                valor=result[1],
                forma_pagamento=result[2],
                multa_mora=result[3],
                juros_mora=result[4],
                correcao_monetaria=result[5],
                prazo_duracao=result[6],
                contratante_id=result[7],
                contratado_id=result[8]
            )
    except Exception as e:
        print(f"Erro ao buscar o contrato empresarial com ID {id}: {str(e)}")
    return None

def update_empresarial(self, contract_id: int, valor: str, forma_pagamento: str, multa_mora: str, juros_mora: str, correcao_monetaria: str, prazo_duracao: str, contratante_id: int, contratado_id: int):
    try:
        # Verifique se o contrato existe
        contrato = self.get_empresarial_by_id(contract_id)
        if not contrato:
            print(f"Contrato com ID {contract_id} não encontrado.")
            return None

        # Atualiza o contrato
        query = """
            UPDATE contracts.empresarial_contract
            SET
                valor = %s,
                forma_pagamento = %s,
                multa_mora = %s,
                juros_mora = %s,
                correcao_monetaria = %s,
                prazo_duracao = %s,
                contratante_id = %s,
                contratado_id = %s
            WHERE id = %s
            RETURNING id, valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao, contratante_id, contratado_id;
        """
        params = (valor, forma_pagamento, multa_mora, juros_mora, correcao_monetaria, prazo_duracao, contratante_id, contratado_id, contract_id)
        _query = self.db.query(query, params)
        if _query and len(_query) > 0:
            result = _query[0]
            return EmpresarialContract(
                id=result[0],
                valor=result[1],
                forma_pagamento=result[2],
                multa_mora=result[3],
                juros_mora=result[4],
                correcao_monetaria=result[5],
                prazo_duracao=result[6],
                contratante_id=result[7],
                contratado_id=result[8]
            )
    except Exception as e:
        print(f"Erro ao atualizar o contrato empresarial com ID {contract_id}: {str(e)}")
    return None

def delete_empresarial_contract(self, id: int):
    try:
        # Verifique se o contrato existe antes de tentar deletar
        contrato = self.get_empresarial_by_id(id)
        if not contrato:
            print(f"Contrato com ID {id} não encontrado.")
            return

        query = "DELETE FROM contracts.empresarial_contract WHERE id = %s"
        self.db.query(query, (id,))
        print(f"Contrato empresarial com ID {id} deletado com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar o contrato empresarial com ID {id}: {str(e)}")


# =========================== CONTRATADO CRUD ===========================

def create_contratado(self, nome: str, nacionalidade: str, estadocivil: str, cpf: str, profissao: str, endereco: str):
    try:
        query = """
            INSERT INTO contracts.contratada (nome, nacionalidade, estadocivil, cpf, profissao, endereco)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id, nome, nacionalidade, estadocivil, cpf, profissao, endereco
        """
        params = (nome, nacionalidade, estadocivil, cpf, profissao, endereco)
        _query = self.db.query(query, params)
        if _query and len(_query) > 0:
            result = _query[0]
            return EmpresarialPerson(
                id=result[0],
                nome=result[1],
                nacionalidade=result[2],
                estadocivil=result[3],
                cpf=result[4],
                profissao=result[5],
                endereco=result[6]
            )
    except Exception as e:
        print(f"Erro ao criar o contratado: {str(e)}")
    return None

def get_all_contratado(self):
    try:
        query = "SELECT * FROM contracts.contratada"
        _query = self.db.query(query)

        if not _query:
            raise Exception('Nenhum registro encontrado')

        return [
            EmpresarialPerson(
                id=row[0],  # Incluindo o ID
                nome=row[1], nacionalidade=row[2], estadocivil=row[3],
                cpf=row[4], profissao=row[5], endereco=row[6]
            ) for row in _query
        ]
    except Exception as e:
        print(f"Erro ao buscar todos os contratados: {str(e)}")
    return []

def update_contratado(self, id: int, nome: str, nacionalidade: str, estadocivil: str, cpf: str, profissao: str, endereco: str):
    try:
        query = """
            UPDATE contracts.contratada
            SET nome = %s, nacionalidade = %s, estadocivil = %s, cpf = %s, profissao = %s, endereco = %s
            WHERE id = %s
            RETURNING id, nome, nacionalidade, estadocivil, cpf, profissao, endereco;
        """
        params = (nome, nacionalidade, estadocivil, cpf, profissao, endereco, id)
        _query = self.db.query(query, params)
        if _query and len(_query) > 0:
            result = _query[0]
            return EmpresarialPerson(
                id=result[0],  # Incluindo o ID atualizado
                nome=result[1],
                nacionalidade=result[2],
                estadocivil=result[3],
                cpf=result[4],
                profissao=result[5],
                endereco=result[6]
            )
    except Exception as e:
        print(f"Erro ao atualizar o contratado com ID {id}: {str(e)}")
    return None

def delete_contratado(self, id: int):
    try:
        query = "DELETE FROM contracts.contratada WHERE id = %s"
        self.db.query(query, (id,))
        print(f"Contratado com ID {id} deletado com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar o contratado com ID {id}: {str(e)}")

def get_contratado_by_id(self, id: str):
    try:
        query = "SELECT * FROM contracts.contratada WHERE id = %s"
        _query = self.db.query(query, (id,))
        if _query and len(_query) > 0:
            result = _query[0]
            return EmpresarialPerson(
                id=result[0],  # Incluindo o ID
                nome=result[1],
                nacionalidade=result[2],
                estadocivil=result[3],
                cpf=result[4],
                profissao=result[5],
                endereco=result[6]
            )
    except Exception as e:
        print(f"Erro ao buscar o contratado com ID {id}: {str(e)}")
    return None

# =========================== CONTRATANTE CRUD ===========================

def create_contratante(self, nome: str, nacionalidade: str, estadocivil: str, cpf: str, profissao: str, endereco: str):
    try:
        query = """
            INSERT INTO contracts.contratante (nome, nacionalidade, estadocivil, cpf, profissao, endereco)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id, nome, nacionalidade, estadocivil, cpf, profissao, endereco;
        """
        params = (nome, nacionalidade, estadocivil, cpf, profissao, endereco)
        _query = self.db.query(query, params)
        if _query and len(_query) > 0:
            result = _query[0]
            return EmpresarialPerson(
                id=result[0],
                nome=result[1],
                nacionalidade=result[2],
                estadocivil=result[3],
                cpf=result[4],
                profissao=result[5],
                endereco=result[6]
            )
    except Exception as e:
        print(f"Erro ao criar o contratante: {str(e)}")
    return None

def get_all_contratante(self):
    try:
        query = "SELECT * FROM contracts.contratante"
        _query = self.db.query(query)

        if not _query:
            raise Exception('Nenhum registro encontrado')

        return [
            EmpresarialPerson(
                id=row[0],  # Incluindo o ID
                nome=row[1], nacionalidade=row[2], estadocivil=row[3],
                cpf=row[4], profissao=row[5], endereco=row[6]
            ) for row in _query
        ]
    except Exception as e:
        print(f"Erro ao buscar todos os contratantes: {str(e)}")
    return []

def update_contratante(self, id: int, nome: str, nacionalidade: str, estadocivil: str, cpf: str, profissao: str, endereco: str):
    try:
        query = """
            UPDATE contracts.contratante
            SET nome = %s, nacionalidade = %s, estadocivil = %s, cpf = %s, profissao = %s, endereco = %s
            WHERE id = %s
            RETURNING id, nome, nacionalidade, estadocivil, cpf, profissao, endereco;
        """
        params = (nome, nacionalidade, estadocivil, cpf, profissao, endereco, id)
        _query = self.db.query(query, params)
        if _query and len(_query) > 0:
            result = _query[0]
            return EmpresarialPerson(
                id=result[0],  # Incluindo o ID atualizado
                nome=result[1],
                nacionalidade=result[2],
                estadocivil=result[3],
                cpf=result[4],
                profissao=result[5],
                endereco=result[6]
            )
    except Exception as e:
        print(f"Erro ao atualizar o contratante com ID {id}: {str(e)}")
    return None

def delete_contratante(self, id: int):
    try:
        query = "DELETE FROM contracts.contratante WHERE id = %s"
        self.db.query(query, (id,))
        print(f"Contratante com ID {id} deletado com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar o contratante com ID {id}: {str(e)}")

def get_contratante_by_id(self, id: int):
    try:
        query = "SELECT * FROM contracts.contratante WHERE id = %s"
        _query = self.db.query(query, (id,))
        if _query and len(_query) > 0:
            result = _query[0]
            return EmpresarialPerson(
                id=result[0],  # Incluindo o ID
                nome=result[1],
                nacionalidade=result[2],
                estadocivil=result[3],
                cpf=result[4],
                profissao=result[5],
                endereco=result[6]
            )
    except Exception as e:
        print(f"Erro ao buscar o contratante com ID {id}: {str(e)}")
    return None
