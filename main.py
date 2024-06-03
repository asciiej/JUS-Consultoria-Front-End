
import sys
import os

# Adicionando o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '.')))

#Importando Classes e Funçoes
from src.interfaceTemporaria import interface
from src.utilitarios.conexao import PostgreSQLConnection
from src.classes.contrato.ContractModel import ContractManager
from src.classes.contrato.ContractControler import ContractControler
from src.classes.usuario.UsuarioModel import UsuarioManager
from src.classes.usuario.UsuarioControler import UsuarioControler

if __name__ == "__main__":
  db_cfg = {
    'host': "buzutyolmqat5dwhefa2-postgresql.services.clever-cloud.com",
    'database': "buzutyolmqat5dwhefa2",
    'user': "uxzvrjoyrvfzlsd1rckj",
    'password': "wKlpuuKPAOS3c6bRodVc590BRJ14K7",
    'port': 50013
  }

  #Instanciando a DB
  db = PostgreSQLConnection(db_cfg)

  #Instanciando os Manager passando a instância da DB separatamente em um dict.

  managers = {
    'contract': ContractManager(db),
    'usuario': UsuarioManager(db)
  }

  #Instanciando os Controlers passando as instâncias dos Managers separadamente em um dict.

  controlers = {
    'contract': ContractControler(managers['contract']),
    'usuario': UsuarioControler(managers['usuario'])
  }

  # TESTES

  # Teste de manager e controler devem ser feitos diretamente daqui

  # Exemplo:

  contract_data = {
    'nome_empresa': 'empresaX',
    'cnpj': '2222321312',
    'cnae_principal': '222',
    'cnae_secundario': '111',
    'cfop_principais': '3213',
    'industria_setor': 'corretora',
    'receita_anual': '10000'
  }

  controlers['contract'].arbitragem(contract_data).create()

  #Iniciando a interface passando o dict com as instâncias dos controlers.
  # interface(controlers)
