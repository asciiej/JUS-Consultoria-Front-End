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
from src.classes.contrato.ContractControler import TributariaControler


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
    contract_data = {
      'nome_empresa': 'empresaX',
      'cnpj': '23212',
      'cnae_principal': '222',
      'cnae_secundario': '111',
      'cfop_principais': '3213',
      'industria_setor': 'corretora',
      'receita_anual': '10000'
    }

    # controlers['contract'].tributaria(contract_data).create()

    # contract_data_tributaria = {
    #   'nome_empresa': 'Empresa X', 
    #   'cnpj': '13', 
    #   'cnae_principal': '125', 
    #   'cnae_secundario':'587', 
    #   'cfop_principais': '654', 
    #   'industria_setor': 'Eletronico', 
    #   'receita_anual': '2000000'
    # }  

    # controlers['contract'].arbitragem(contract_data).create()
    # managers['contract'].create_tributaria_contract(contract_data_tributaria)
    # managers['contract'].alterarDadosContrato(8, "Empresa lucas", "684", "793", "47", "456", "Varejo", 77549)

    # teste8 = managers['contract'].getTributariaContract()
    # for item in teste8:
    #   print(" | ".join(map(str, item)))

    # teste1 = managers['usuario'].getUserByCPF('987.654.321-00')
    # teste2 = managers['usuario'].getUserByEmail('xxx@pwi.com.br')
    # print(teste1)
    # print(teste2)

    # teste22 = managers['usuario'].getAllUsers()
    # print(teste22)

    contract_data_empresarial = {
      'contratante': 'empresaX',
      'contratado': 'empresaY',
      'valor': '1000',
      'forma_pagamento': 'pix',
      'multa_mora': '10',
      'juros_mora': '5',
      'correcao_monetaria': '20',
      'prazo_duracao': '12'
    }
     

    # managers['contract'].create_empresarial_contract(contract_data_empresarial)
    # managers['contract'].alterarDadosContratoEmpresarial(contract_id= 3, contratante="Empresa PWI", contratado='Maurico', valor='400', forma_pagamento='Debito', multa_mora='15', juros_mora='2', correcao_monetaria='10', prazo_duracao='6')

    teste8 = managers['contract'].getEmpresarialContract()
    for item in teste8:
      print(" | ".join(map(str, item)))

    # teste7 = managers['contract'].getEmpresarialContract()
  

    # teste3 = controlers['usuario'].cadastro(nome="Matheus", sobrenome="Canteiro", cpf="526.614.888-80", nomeEmpresa="Adega Heliopolis", cargo="Empresario", eMail="biso@zenk.com.br", telefone="+55 11 90002-3333", pais="Campinas", senha="lago", confirmeSenha="lago")
    # teste4 = controlers['usuario'].alterarDadosUsuario(
    #     cpf = "987.654.321-00",
    #     nome = "Murilo",
    #     sobrenome = "Beppler",
    #     nomeEmpresa = "SimCorp",
    #     cargo = "Engenheiro de Cozinha",
    #     email = "carlos.Moutinho@example.com",
    #     telefone = "+55 12 34567-8901",
    #     pais = "EUA",
    #     senha = "NovaSenha",
    #     novaSenha= "NovaSenha",
    #     confirmeNovaSenha= "NovaSenha"
    # )

    # print(teste4)


  #Iniciando a interface passando o dict com as instâncias dos controlers.
  # interface(controlers)
