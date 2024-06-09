# Como dar GET em contratos

## Usando a interface

Essa função foi criada para ser usado exclusivamente na interface, ela automatiza a chamada das funções para o crud dos contratos

```python
def get_contract_by_id(contract_type, contract_id):
  # getattr é uma função que dispara outra função/metodo que foi passado como parametro
  # controlers['contract'] é a classe ContractControler
  # contract_type é o metodo da classe acima que vai ser chamado (nome exato)
  # o getattr chama e retorna a classe que foi passada no contract_type...
  # ...possibilitando chamar outros metodos que estao nessa classe, como o get_by_id()
  return getattr(controlers['contract'], contract_type)().get_by_id(contract_id)
```
Como a interface esta chamando

```python
# Parametros: Frame - Nome Botao - Função/Metodo - Tipo Contrato - ID
create_button(frame, "GET Contract", get_contract_by_id, 'empresarial', 2)
```

## Usando em outros lugares

> ### Cada Classe tem seus metodos (ate o momento todas tem os mesmos)
>
> #### Classes - Contratos
>
> - empresarial
> - arbitragem
> - tributaria
>
> #### Metodos - Crud [GET]
>
>
> - get_all()
> - get_by_id(contract_id)
>
> Exemplo:
>
> ```python
> controlers['contract'].empresarial().get_by_id(contract_id)
> ```
> <br>
