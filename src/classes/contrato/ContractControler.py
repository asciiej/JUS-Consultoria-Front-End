from .ContractModel import ContractManager

class ContractControler:
  def __init__(self, manager) -> None:
    self.contract_manager = manager

  def arbitragem(self, contract_data):
    return ArbitragemControler(contract_data, self.contract_manager)

  def tributaria(self, contract_data):
    return TributariaControler(contract_data, self.contract_manager)

  def empresarial(self, contract_data):
    return EmpresarialControler(contract_data, self.contract_manager)


class ArbitragemControler():
  def __init__(self, contract_data, manager):
    self.contract = contract_data
    self.manager = manager

  def create(self):
    print('criando contrato arbitragem')
    self.manager.create_arbitragem_contract(self.contract)

class TributariaControler():
  def __init__(self, contract_data, manager):
    self.contract = contract_data
    self.manager = manager

  def create(self):
    print('criando contrato tributaria')
    self.manager.create_tributaria_contract(self.contract)


class EmpresarialControler():
  def __init__(self, contract_data, manager):
    self.contract = contract_data
    self.manager = manager

  def create(self):
    print('criando contrato empresarial')
    self.manager.create_empresarial_contract(self.contract)

