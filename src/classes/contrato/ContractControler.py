import config
from .ContractModel import ContractManager
from src.utilitarios.operacoesDocumento import split_string,recombine_string

class ContractControler:
  def __init__(self, manager):
    self.contract_manager = manager

  def arbitragem(self, contract_data=None):
    return ArbitragemControler(self.contract_manager, contract_data)

  def tributaria(self, contract_data=None):
    return TributariaControler(self.contract_manager, contract_data)

  def empresarial(self, contract_data=None):
    return EmpresarialControler(self.contract_manager, contract_data)
  
  def contratante(self, contratante_data=None):
    return ContratanteControler(self.contract_manager, contratante_data)
  
  def contratado(self, contratado_data=None):
    return ContratadoControler(self.contract_manager, contratado_data)

  def modeloDeContrato(self, contract_data=None):
    return ModeloDeContratoControler(self.contract_manager, contract_data)

class Controler():
  def __init__(self, manager, contract_data=None):
    self.manager = manager
    self.contract = contract_data

class ArbitragemControler(Controler):
  def create(self):
    return self.manager.create_arbitragem(self.contract['nome_empresa'], self.contract['cnpj'], self.contract['cnae_principal'], self.contract['cnae_secundaria'], self.contract['cfop_principais'], self.contract['industria_setor'], self.contract['receita_anual'])

class TributariaControler(Controler):
  def create(self):
    return self.manager.create_tributaria(self.contract['nome_empresa'], self.contract['cnpj'], self.contract['cnae_principal'], self.contract['cnae_secundaria'], self.contract['cfop_principais'], self.contract['industria_setor'], self.contract['receita_anual'])

  def get_by_id(self, contract_id):
    return self.manager.get_tributaria_by_id(contract_id)

  def get_all(self):
    return self.manager.get_all_tributaria()

  def update(self, contract_id):
    return self.manager.update_tributaria(contract_id, self.contract['nomeEmpresa'], self.contract['cnpj'], self.contract['cnaePrincipal'], self.contract['cnaeSecundaria'], self.contract['cfopPrincipais'], self.contract['industriaSetor'], self.contract['receitaAnual'])

  def delete(self, contract_id):
    return self.manager.delete_tributaria(contract_id)

class EmpresarialControler(Controler):
  def create(self):
    contratante_id = self.manager.create_contratante(self.contract['contratante'])
    contratado_id = self.manager.create_contratado(self.contract['contratado'])
    return self.manager.create_empresarial_contract(
            contratante_id,
            contratado_id,
            self.contract['valor'],
            self.contract['forma_pagamento'],
            self.contract['multa_mora'],
            self.contract['juros_mora'],
            self.contract['correcao_monetaria'],
            self.contract['prazo_duracao']
        )

  def get_by_id(self, contract_id):
    return self.manager.get_empresarial_by_id(contract_id)

  def get_all(self):
    return self.manager.get_all_empresarial()

  def update(self, contract_id):
        return self.manager.update_empresarial(
            contract_id,
            self.contract
        )

  def delete(self, contract_id):
    return self.manager.delete_empresarial_contract(contract_id)
  
class ContratanteControler(Controler):
  def create(self):
    return self.manager.create_contratante(self.contract['nome'], self.contract['nacionalidade'], self.contract['estadocivil'], self.contract['cpf'], self.contract['profissao'], self.contract['endereco'])

  def get_contratante_by_id(self, contratante_id):
    return self.manager.get_contratante_by_id(contratante_id)
  
  def get_all_contratante(self):
    return self.manager.get_all_contratante()
  
  def update(self, contratante_id):
    return self.manager.update_contratante(contratante_id)
  
  def delete(self, contratante_id):
    return self.manager.delete_contratante(contratante_id)
  
class ContratadoControler(Controler):
  def create(self):
    return self.manager.create_contratado(self.contract['nome'], self.contract['nacionalidade'], self.contract['estadocivil'], self.contract['cpf'], self.contract['profissao'], self.contract['endereco'])

  def get_contratado_by_id(self, contratado_id):
    return self.manager.get_contratado_by_id(contratado_id)
  
  def get_all_contratado(self):
    return self.manager.get_all_contratado()
  
  def update(self, contratado_id):
    return self.manager.update_contratado(contratado_id)
  
  def delete(self, contratado_id):
    return self.manager.delete_contratado(contratado_id)



class ModeloDeContratoControler(Controler):
  def create(self):
    textoContrato = split_string(self.contract["textoContrato"])
    self.manager.create_contract_model(self.contract["tituloContrato"],self.contract["tipoContrato"],textoContrato)

  def get_by_id(self,id):
    retornoBD =  self.manager.get_contract_model_byId(id)
    return self.recombine_contract(retornoBD)

  def get_by_title(self,title):
    retornoBD = self.manager.get_contract_model_byTitle(title)
    return self.recombine_contract(retornoBD)

  def recombine_contract(self,tuples_list):
    nova_lista = []
    # Itera sobre cada tupla na lista original
    for tupla in tuples_list:
        # Extrai o terceiro e o primeiro elementos da tupla original
        novo_elemento = (tupla[2], tupla[0])
        # Adiciona a nova tupla à nova lista
        nova_lista.append(novo_elemento)

    return recombine_string(nova_lista)