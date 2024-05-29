
import sys
import os

# Adicionando o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '.')))

#Importando Classes e Funçoes
from interfaceTemporaria import interface
from src.utilitarios.conexao import PostgreSQLConnection
from src.classes.contrato.ContractModel import ContractManager
from src.classes.contrato.ContractControler import ContractControler

if __name__ == "__main__":
  db_cfg = {
    'host': "buzutyolmqat5dwhefa2-postgresql.services.clever-cloud.com",
    'database': "buzutyolmqat5dwhefa2",
    'user': "uxzvrjoyrvfzlsd1rckj",
    'password': "wKlpuuKPAOS3c6bRodVc590BRJ14K7",
    'port': 50013
  }

  #Instanciando a DB
  db = PostgreSQLConnection()

  #Instanciando o ContractManager passando a instância da DB
  contract_manager = ContractManager(db)

  #Instanciando o ContractControler passando a instância do ContractManager
  contract_controler = ContractControler(contract_manager)

  #Iniciando a interface passando a instância do ContractControler
  interface(contract_controler)
