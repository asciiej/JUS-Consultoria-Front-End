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

  # TESTES

  # Teste de manager e controler devem ser feitos diretamente daqui

  if config.DEBUG:
    # contract_data = {
    #   'nome_empresa': 'empresaX',
    #   'cnpj': '2222321312',
    #   'cnae_principal': '222',
    #   'cnae_secundario': '111',
    #   'cfop_principais': '3213',
    #   'industria_setor': 'corretora',
    #   'receita_anual': '10000'
    # }

    # controlers['contract'].arbitragem(contract_data).create()

    teste1 = managers['usuario'].getUserByCPF('987.654.321-00')
    # teste2 = managers['usuario'].getUserByEmail('bruna.santos@example.com')
    print(teste1)

    # teste3 = controlers['usuario'].cadastro(nome="Bruna", sobrenome="Santos", cpf="987.654.321-00", nomeEmpresa="TechCorp", cargo="Engenheira de Software", eMail="bruna.santos@example.com", telefone="+55 12 34567-8901", pais="Brasil", senha="P@ssw0rd", confirmeSenha="P@ssw0rd")
    # teste4 = controlers['usuario'].alterarDadosUsuario(
    #     cpf = "987.654.321-00",
    #     nome = "Carlos",
    #     sobrenome = "Santos",
    #     nomeEmpresa = "SimCorp",
    #     cargo = "Engenheiro de Cozinha",
    #     email = "carlos.santos@example.com",
    #     telefone = "+55 12 34567-8901",
    #     pais = "EUA",
    #     senha = "Teste",
    #     novaSenha= "Teste2",
    #     confirmeNovaSenha= "Teste2"
    # )

    # print(teste4)


  #Iniciando a interface passando o dict com as instâncias dos controlers.
  # interface(controlers)