import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '.')))

# from src.interface.login import telaLogin
# from src.classes.usuario.usuarioControler import usuarioControler
# from src.classes.contrato.contract_management import contractManager
from src.interface import interface
from src.utilitarios.conexao import PostgreSQLConnection
from src.classes.contrato.ContractModel import ContractManager
from src.classes.contrato.ContractControler import ContractControler
# usuarioControler().cadastro("Lucas","Sabbatini Janot Procópio","700.302.181-10","ASCII","Programador","lucas.exemplo@ufu.br","+55 12 34567-8901","Brasil","luc@s123","luc@s123")
# usuarioControler().login("lucas.exemplo@ufu.br","luc@s123")

# print(contractManager().listaContratos())

if __name__ == "__main__":
  db = PostgreSQLConnection()

  contract_manager = ContractManager(db)

  contract_controler = ContractControler(contract_manager)

  interface(contract_controler)
