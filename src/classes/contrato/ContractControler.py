import config
from src.utilitarios.operacoesDocumento import split_string,recombine_string

class ContractControler:
  def __init__(self, manager):
    self.contract_manager = manager

  def arbitragem(self, contract_data=[]):
    return ArbitragemControler(self.contract_manager, contract_data)

  def tributaria(self, contract_data=[]):
    return TributariaControler(self.contract_manager, contract_data)

  def empresarial(self, contract_data=[]):
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

class ContratanteControler(Controler):
  def create(self, contratante_data):
    return self.manager.create_contratante(contratante_data['nome'], contratante_data['nacionalidade'], contratante_data['estadocivil'], contratante_data['cpf'], contratante_data['profissao'], contratante_data['endereco'])

  def get_contratante_by_id(self, contratante_id):
    return self.manager.get_contratante_by_id(contratante_id)

  def get_all_contratante(self):
    return self.manager.get_all_contratante()

  def update(self, contratante_id, contratante_data):
    return self.manager.update_contratante(contratante_id, contratante_data['nome'], contratante_data['nacionalidade'], contratante_data['estadocivil'], contratante_data['cpf'], contratante_data['profissao'], contratante_data['endereco'])

  def delete(self, contratante_id):
    return self.manager.delete_contratante(contratante_id)

class ContratadoControler(Controler):
  def create(self, contratado_data):
    return self.manager.create_contratado(contratado_data['nome'], contratado_data['nacionalidade'], contratado_data['estadocivil'], contratado_data['cpf'], contratado_data['profissao'], contratado_data['endereco'])

  def get_contratado_by_id(self, contratado_id):
    return self.manager.get_contratado_by_id(contratado_id)

  def get_all_contratado(self):
    return self.manager.get_all_contratado()

  def update(self, contratado_id, contratado_data):
    return self.manager.update_contratado(contratado_id, contratado_data['nome'], contratado_data['nacionalidade'], contratado_data['estadocivil'], contratado_data['cpf'], contratado_data['profissao'], contratado_data['endereco'])

  def delete(self, contratado_id):
    return self.manager.delete_contratado(contratado_id)

class EmpresarialControler(Controler):
  def create(self):
    contratante = ContratanteControler.create(self, self.contract['contratante'])
    contratado = ContratadoControler.create(self, self.contract['contratado'])
    return self.manager.create_empresarial_contract(
      self.contract['valor'],
      self.contract['forma_pagamento'],
      self.contract['multa_mora'],
      self.contract['juros_mora'],
      self.contract['correcao_monetaria'],
      self.contract['prazo_duracao'],
      contratante.id,
      contratado.id,
    )

  def get_by_id(self, contract_id):
    return self.manager.get_empresarial_by_id(contract_id)

  def get_all(self):
    return self.manager.get_all_empresarial()

  def update(self, contract_id):
    contratante_id = self.manager.get_empresarial_by_id(contract_id).contratante_id
    contratado_id = self.manager.get_empresarial_by_id(contract_id).contratado_id

    contratante = ContratanteControler.update(self, contratante_id, self.contract['contratante'])
    contratado = ContratadoControler.update(self, contratado_id, self.contract['contratado'])
    return self.manager.update_empresarial(
      contract_id,
      self.contract['valor'],
      self.contract['forma_pagamento'],
      self.contract['multa_mora'],
      self.contract['juros_mora'],
      self.contract['correcao_monetaria'],
      self.contract['prazo_duracao'],
      contratante.id,
      contratado.id
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
    if not self.manager.get_contract_model_byTitle(self.contract["tituloContrato"]):
      self.manager.create_contract_model(self.contract["tituloContrato"],self.contract["tipoContrato"],textoContrato)
    print("Contrato já está cadastrado no banco")
    self.manager.update_contract_model(self.contract["tituloContrato"],textoContrato)

  def get_by_id(self,id):
    retornoBD =  self.manager.get_contract_model_byId(id)
    return self.recombine_contract(retornoBD)

  def get_by_title(self,title):
    retornoBD = self.manager.get_contract_model_byTitle(title)
    return self.recombine_contract(retornoBD)

  def recombine_contract(self,tuples_list):
    nova_lista = []
    for tupla in tuples_list:
      novo_elemento = (tupla[2], tupla[0])
      nova_lista.append(novo_elemento)

    return recombine_string(nova_lista)