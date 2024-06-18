from typing import Dict, Union
import sys
import os
import config

# Adicionando o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '.')))

#Importando Classes e Funçoes
from src.interfaceTemporaria import interface
from src.utilitarios.conexao import PostgreSQLConnection
from src.classes.contrato.ContractModel import ContractManager
from src.classes.contrato.ContractControler import ContractControler
from src.classes.contrato.ContractControler import EmpresarialControler
from src.classes.usuario.UsuarioModel import UsuarioManager
from src.classes.usuario.UsuarioControler import UsuarioControler
from src.interface.login import TelaLogin


# TODO: Testar todo o CRUD dos contratos novamente
if __name__ == "__main__":
  #Instanciando a DB
  db = PostgreSQLConnection(config.DATABASE_URL)

  #Instanciando os Manager passando a instância da DB separatamente em um dict.
  managers: Dict[str, Union[ContractManager, UsuarioManager]] = {
    'contract': ContractManager(db),
    'usuario': UsuarioManager(db)
  }

  #Instanciando os Controlers passando as instâncias dos Managers separadamente em um dict.
  controlers: Dict[str, Union[ContractControler, UsuarioControler]] = {
    'contract': ContractControler(managers['contract']),
    'usuario': UsuarioControler(managers['usuario'])
  }

  # TelaLogin(controlers)

  #Iniciando a interface passando o dict com as instâncias dos controlers.
  # interface(controlers)

if config.DEBUG:
    contratante_data = {
            'nome': 'Empresa X',
            'nacionalidade': 'brasileiro',
            'estadocivil': 'solteiro',
            'cpf': '89363329100',
            'profissao': 'roupeiro',
            'endereco': 'Rua 123'
        }
    contratado_data = {
            'nome': 'Empresa Y',
            'nacionalidade': 'brasileiro',
            'estadocivil': 'solteiro',
            'cpf': '70670815136',
            'profissao': 'padeiro',
            'endereco': 'Rua 658'
        }

        # Criando contratante e contratado e obtendo seus IDs
    #contratante_id = managers['contract'].create_contratante(**contratante_data)
    #contratado_id = managers['contract'].create_contratado(**contratado_data)

    contratante = managers['contract'].get_contratante_by_id(1)
    contratada = managers['contract'].get_contratado_by_id(1)

        # Dados do contrato empresarial
    contract_data = {
            'valor': 100000.0,
            'forma_pagamento': 'A vista',
            'multa_mora': 2.0,
            'juros_mora': 1.0,
            'correcao_monetaria': 'IPCA',
            'prazo_duracao': '12',
            'contratante_id': contratante,
            'contratado_id': contratada
        }

        # Criando contrato empresarial
    managers['contract'].create_empresarial_contract(
        contract_data['valor'],
        contract_data['forma_pagamento'],
        contract_data['multa_mora'],
        contract_data['juros_mora'],
        contract_data['correcao_monetaria'],
        contract_data['prazo_duracao'],
        contract_data['contratante_id'],
        contract_data['contratado_id']
    )

    # managers['contract'].create_empresarial_contract(100000,)

        # Obtendo e imprimindo todos os contratos empresariais
    all_contracts = controlers['contract'].empresarial().get_all()

    for contract in all_contracts:
        print(contract)
