from typing import Dict, Union
import customtkinter as ctk
import sys
import os
import config

# Adicionando o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '.')))

#Importando Classes e Funçoes
from src.utilitarios.conexao import PostgreSQLConnection
from src.classes.contrato.ContractModel import ContractManager
from src.classes.contrato.ContractControler import ContractControler
from src.classes.usuario.UsuarioModel import UsuarioManager
from src.classes.usuario.UsuarioControler import UsuarioControler

from mainApp import MainApp





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

	contratante_data = {
		'nome': 'AMARAL PWI',
		'nacionalidade': 'angolano',
		'estadocivil': 'solteiro',
		'cpf': '111',
		'profissao': 'roupeiro',
		'endereco': 'Rua dos Peneira'
	}

	contratado_data = {
		'nome': 'ARAUJO PWI',
		'nacionalidade': 'brasileiro',
		'estadocivil': 'casado',
		'cpf': '222',
		'profissao': 'faxineiro',
		'endereco': 'Rua dos Paes'
	}

	contract_data = {
		'valor': '15.99',
		'forma_pagamento': 'CARTAO',
		'multa_mora': '150.00',
		'juros_mora': '25.00',
		'correcao_monetaria': '10.0',
		'prazo_duracao': '10',
		'contratante': contratante_data,
		'contratado': contratado_data
	}

	# controlers['contract'].empresarial(contract_data=contract_data).create()
	# controlers['contract'].empresarial(contract_data=contract_data).update(8)

	# con = controlers['contract'].empresarial().get_by_id(8)
	# print(con.str())
	# controlers['usuario'].login('araujomat@pwi.com', '111')
	# print(controlers['usuario'].get_all_users())


	#MainApp(controlers)
	app = MainApp(controlers)
	app.mainloop()
	# AtualizaCad(controlers)

if config.DEBUG:
	pass
