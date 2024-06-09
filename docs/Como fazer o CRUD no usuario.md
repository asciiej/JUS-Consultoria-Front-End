# Como fazer o CRUD no usuario

## GET

#### RETORNO: Tupla do(s) usuario(s)

```python
  controlers['usuario'].get_user_by_email('l2ZrM@example.com')
  controlers['usuario'].get_user_by_cpf('111.111.111-11')
  controlers['usuario'].get_all_users()
```
## REGISTER

#### PARAMETROS: ***nome***, ***sobrenome***, ***cpf***, ***nome-da-empresa***, ***cargo***, ***emai***, ***telefone***, ***pais***, ***senha***, ***confirmar-senha***
#### RETORNO: Tupla do usuario registrado

```python
  controlers['usuario'].register('Joao', 'Silva', '111.111.111-11', 'JUS', 'Engenheiro de Software', 'l2ZrM@example.com', '+55 12 34567-8901', 'Brasil', '1234', '1234')
```

## UPDATE

O cpf está na frente pois ele é o identificador do usuario.

#### PARAMETROS: ***cpf***, ***nome***, ***sobrenome***, ***nome-da-empresa***, ***cargo***, ***emai***, ***telefone***, ***pais***, ***senha***, ***nova-senha***, ***confirmar-nova-senha***
#### RETORNO: Tupla do usuario atualizado

```python
  controlers['usuario'].update_user('111.111.111-11', 'Joao', 'Silva', 'JUS', 'Engenheiro de Software', 'l2ZrM@example.com', '+55 12 34567-8901', 'Brasil', '1234', '4321', '4321')
```

## DELETE

#### PARAMETROS: ***cpf***
#### RETORNO: Tupla do usuario deletado

```python
  controlers['usuario'].delete_user('111.111.111-11')
```

