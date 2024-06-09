# Logica Managers e Controlers

## Geral - Explicando o funcionamento dos managers e controlers

Cada classe (usuario e contrato) do projeto contém um manager e um controler.
Todos os managers e controlers devem ser importados na main do projeto.
Os controlers devem ser passados na chamada da interface do projeto.

Manager: Responsavel por gerenciar os dados dos usuários e dos contratos no banco de dados.
Controler: Responsavel por processar as requisições da interface dos usuários e dos contratos.

### Main

***Todos os testes que tenham contato com contratos ou usuarios devem ser feitos diretamente na main.***

Importação dos managers e controlers

```python
from src.classes.contrato.ContractModel import ContractManager
from src.classes.contrato.ContractControler import ContractControler
from src.classes.usuario.UsuarioModel import UsuarioManager
from src.classes.usuario.UsuarioControler import UsuarioControler
```

Nessa parte da main, os managers e controlers são instanciados separadamente, cada tipo em seu dict.
Os managers recebem a instância da DB e os controlers recebem as instâncias dos managers

```python
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
```
#### Passando para interface

Na chamada da interface deve ser passado o dict com as instâncias dos controlers

```python
  interface(controlers)
```
No script da interface principal o dict com os controlers deve ser usado dessa maneira.

```python
  # atribuindo o dict com os controlers a uma variável (nesse caso na classe)
  self.controlers = controlers

  # chamando os metodos reference ao controler escolhido
  # contract_data é a variavel que possivelmente vai ser usada para retornar os dados dos contratos
  self.controlers['contract'].empresarial(contract_data).create()
  self.controlers['contract'].empresarial().get_all()

  self.controlers['usuario'].register(...)
  self.controlers['usuario'].get_all_users()
```