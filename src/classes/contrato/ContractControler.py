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
    return self.manager.create_empresarial(self.contract)

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

class ModeloDeContratoControler(Controler):
  def create(self):
    textoContrato = split_string(self.contract["textoContrato"])
    self.manager.create_contract_model(self.contract["tituloContrato"],self.contract["tipoContrato"],textoContrato)