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
    teste2 = managers['usuario'].getUserByEmail('beiso@pwi.com.br')
    print(teste1)
    print(teste2)

    # teste3 = controlers['usuario'].cadastro(nome="Gaspar", sobrenome="Lauri", cpf="469.913.858-67", nomeEmpresa="PWI Sistemas", cargo="Tech Lead", eMail="beiso@pwi.com.br", telefone="+55 16 90002-8922", pais="Angola", senha="P@Sim", confirmeSenha="P@Sim")
    teste4 = controlers['usuario'].alterarDadosUsuario(
        cpf = "987.654.321-00",
        nome = "Murilo",
        sobrenome = "Beppler",
        nomeEmpresa = "SimCorp",
        cargo = "Engenheiro de Cozinha",
        email = "carlos.Moutinho@example.com",
        telefone = "+55 12 34567-8901",
        pais = "EUA",
        senha = "NovaSenha",
        novaSenha= "NovaSenha",
        confirmeNovaSenha= "NovaSenha"
    )

    print(teste4)


  #Iniciando a interface passando o dict com as instâncias dos controlers.
  # interface(controlers)