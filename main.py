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
from src.interface.edicaoContratos import telaEdicaoContrato



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
	# controlers['usuario'].register('Joao', 'Silva', '111.111.111-11', 'JUS', 'Engenheiro de Software', 'l2ZrM@example.com', '+55 12 34567-8901', 'Brasil', '1234', '1234')

	# controlers['usuario'].login('l2ZrM@example.com', '4321')
	# controlers['usuario'].update_user('111.111.111-11','Joao', 'Silva', 'JUS', 'Engenheiro de Software', 'l2ZrM@example.com', '+55 12 34567-8901', 'Brasil', '4321', '1111', '1111')

	#Iniciando a interface passando o dict com as instâncias dos controlers.
	TelaLogin(controlers)

if config.DEBUG:
	pass