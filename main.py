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

  # managers['usuario'].add_role('987.654.321-00', 'admin')
  # print(managers['usuario'].remove_role('987.654.321-00', 'admin'))
  # print(managers['usuario'].has_role('987.654.321-00', 'admin'))

  # TelaLogin(controlers)

  #Iniciando a interface passando o dict com as instâncias dos controlers.
  # interface(controlers)
