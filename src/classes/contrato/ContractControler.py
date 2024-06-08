import config
from src.utilitarios.operacoesDocumento import split_string,recombine_string

class ContractControler:
  def __init__(self, manager):
    self.contract_manager = manager

  def arbitragem(self, contract_data):
    return ArbitragemControler(contract_data, self.contract_manager)

  def tributaria(self, contract_data):
    return TributariaControler(contract_data, self.contract_manager)

  def empresarial(self, contract_data):
    return EmpresarialControler(contract_data, self.contract_manager)
  
  def modeloDeContrato(self,contract_data):
    return ModeloDeContratoControler(contract_data, self.contract_manager)

class Controler():
  def __init__(self, contract_data, manager):
    self.contract = contract_data
    self.manager = manager

class ArbitragemControler(Controler):
  def create(self):
    self.manager.create_arbitragem_contract(self.contract)

    if config.DEBUG:
      print('criando contrato arbitragem')

class TributariaControler(Controler):
  def create(self):
    self.manager.create_tributaria_contract(self.contract)

    if config.DEBUG:
      print('criando contrato tributaria')

class EmpresarialControler(Controler):
  def create(self):
    self.manager.create_empresarial_contract(self.contract)

    if config.DEBUG:
      print('criando contrato empresarial')

class ModeloDeContratoControler(Controler):
  def create(self):
    textoContrato = split_string(self.contract["textoContrato"])
    self.manager.create_contract_model(self.contract["tituloContrato"],self.contract["tipoContrato"],textoContrato)

    if config.DEBUG:
      print('criando modelo de contrato')