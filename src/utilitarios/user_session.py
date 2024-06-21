class USER_SESSION:
  __user_info = { "logged": False, "data": {} }

  @classmethod
  def get_user_info(cls) -> dict:
    """
    Retorna o dicionário com os dados e o status do usuário que estiver logado.

    @return: dicionário com os dados e o status do usuário

    @rtype: dict

    @example:
    >>> USER_SESSION.get_user_info()
    { "logged": False, "data": {...Dados Usuario...} }
    """
    return cls.__user_info

  @classmethod
  def set_user_info(cls, data) -> None:
    """
    Atualiza o dicionário com os dados do usuário que estiver logado.

    @param data: retorno da DB com os dados do usuário

    @example:
    >>> USER_SESSION.set_user_info(...Dados Usuario...)
    """
    cls.__user_info['data'] = data
    cls.__user_info['logged'] = True  # Atualizando o status de login

  @classmethod
  def clear_user_info(cls) -> None:
    """
    Limpa o dicionário com os dados do usuário que estiver logado.

    @example:
    >>> USER_SESSION.clear_user_info()
    """
    cls.__user_info = { "logged": False, "data": {} }

  @classmethod
  def get_user_data(cls) -> dict:
    """
    Retorna o dicionário com os dados do usuário que estiver logado.

    @return: dicionário com os dados do usuário

    @rtype: dict

    @example:
    >>> USER_SESSION.get_user_data()
    {...Dados Usuario...}
    """
    return cls.__user_info["data"]

  @classmethod
  def is_logged(cls):
    """
    Retorna o status de login do usuário.

    @return: status de login

    @rtype: bool

    @example:
    >>> USER_SESSION.is_logged()
    True
    """
    return cls.__user_info["logged"]

  @classmethod
  def has_role(cls, role):
    """
    Retorna se o usuário tem a role informada.

    @param role: role que o usuário deve ter

    @return: se o usuário tem a role informada

    @rtype: bool

    @example:
    >>> USER_SESSION.has_role('admin')
    True
    """
    return role in cls.__user_info["data"].roles

  @classmethod
  def is_admin(cls):
    """
    Retorna se o usuário é admin.

    @return: se o usuário é admin

    @rtype: bool

    @example:
    >>> USER_SESSION.is_admin()
    True
    """
    return 'admin' in cls.__user_info["data"].roles
