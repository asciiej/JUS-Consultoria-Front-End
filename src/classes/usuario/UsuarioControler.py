from .UsuarioModel import DatabaseConselt
from ...utilitarios.excecoes import (
    CargoInvalido, EmailInvalido, NomeInvalido, PaisInvalido,
    CPFInvalido, NomeEmpresaInvalido, SenhaInvalido, TelefoneInvalido, UsuarioOuSenhaInvalido
)
from ...utilitarios.check import Check
from ...utilitarios.user_session import USER_SESSION
import config
import hashlib

class UsuarioControler:
    def __init__(self, usuario_manager):
        self.usuario_manager = usuario_manager
        self.conselt_manager =  DatabaseConselt()

    def login(self, email: str, senha: str):
        try:
            if not Check.Email(email):
                raise EmailInvalido(email)

            if ' ' in senha:
                raise SenhaInvalido()

            senha_hash = self._calcular_sha256(senha)

            # Realiza o login através do manager
            usuario = self.usuario_manager.login(email, senha_hash)
            if usuario is None:
                usuario = self.get_user_by_email_conselt(email,senha)
            USER_SESSION.set_user_info(usuario)

            return True

        except EmailInvalido as e:
            if config.DEBUG:
                print(f"Erro ao efetuar login: {str(e)}")
            return False

        except SenhaInvalido as e:
            if config.DEBUG:
                print(f"Erro ao efetuar login: {str(e)}")
            return False

        except Exception as e:
            if config.DEBUG:
                print(f"Erro ao efetuar login: {str(e)}")
            return False

    def register(self, nome: str, sobrenome: str, cpf: str, nome_empresa: str, cargo: str, email: str, telefone: str, pais: str, senha: str, confirme_senha: str):
        try:
            self._validate_input(nome, sobrenome, cpf, nome_empresa, cargo, email, telefone, pais, senha, confirme_senha)

            senha_hash = self._calcular_sha256(senha)

            return self.usuario_manager.create(nome, sobrenome, cpf, nome_empresa, cargo, email, telefone, pais, senha_hash)

        except (
            NomeInvalido, EmailInvalido, TelefoneInvalido,
            CargoInvalido, NomeEmpresaInvalido, PaisInvalido,
            SenhaInvalido, CPFInvalido
        ) as e:
            if config.DEBUG:
                print(f"Erro ao registrar usuário: {str(e)}")
            return None

        except Exception as e:
            if config.DEBUG:
                print(f"Erro ao registrar usuário: {str(e)}")
            return None

    def update_user(self, cpf: str, nome: str, sobrenome: str, nome_empresa: str, cargo: str, email: str, telefone: str, pais: str, senha_atual: str, nova_senha: str, confirme_nova_senha: str):
        try:
            self._validate_input(nome, sobrenome, cpf, nome_empresa, cargo, email, telefone, pais, nova_senha, confirme_nova_senha)

            if not self._validar_senha_atual(senha_atual, cpf):
                print(senha_atual, cpf)
                raise SenhaInvalido()

            nova_senha_hash = self._calcular_sha256(nova_senha)

            updated = self.usuario_manager.update(cpf, nome, sobrenome, nome_empresa, cargo, email, telefone, pais, nova_senha_hash)
            USER_SESSION.set_user_info(updated)
            return True

        except (
            NomeInvalido, EmailInvalido, TelefoneInvalido,
            CargoInvalido, NomeEmpresaInvalido, PaisInvalido,
            SenhaInvalido, CPFInvalido
        ) as e:
            if config.DEBUG:
                print(f"Erro ao atualizar usuário: {str(e)}")
            return None

        except Exception as e:
            if config.DEBUG:
                print(f"Erro ao atualizar usuário: {str(e)}")
            return None

    def delete_user(self, cpf: str):
        try:
            if 'admin' not in USER_SESSION.get_user_data().roles:
                raise Exception("Necessário permissão de administrador.")

            if not Check.CPF(cpf):
                raise CPFInvalido(cpf)

            return self.usuario_manager.delete(cpf)

        except CPFInvalido as e:
            if config.DEBUG:
                print(f"Erro ao excluir usuário: {str(e)}")
            return None

        except Exception as e:
            if config.DEBUG:
                print(f"Erro ao excluir usuário: {str(e)}")
            return None

    def get_all_users(self):
        try:
            if 'admin' not in USER_SESSION.get_user_data().roles:
                raise Exception("Necessário permissão de administrador.")

            return self.usuario_manager.get_all()

        except Exception as e:
            if config.DEBUG:
                print(f"Erro ao obter todos os usuários: {str(e)}")
            return []

    def get_user_by_cpf(self, cpf: str):
        try:
            return self.usuario_manager.get_by_cpf(cpf)

        except Exception as e:
            if config.DEBUG:
                print(f"Erro ao obter usuário por CPF {cpf}: {str(e)}")
            return None

    def get_user_by_email(self, email: str):
        try:
            return self.usuario_manager.get_by_email(email)

        except Exception as e:
            if config.DEBUG:
                print(f"Erro ao obter usuário por e-mail {email}: {str(e)}")
            return None

    def user_has_role(self, cpf: str, role: str):
        try:
            return self.usuario_manager.has_role(cpf, role)

        except Exception as e:
            if config.DEBUG:
                print(f"Erro ao verificar papel do usuário: {str(e)}")
            return False

    def user_add_role(self, cpf: str, role: str):
        try:
            if 'admin' not in USER_SESSION.get_user_data().roles:
                raise Exception("Necessário permissão de administrador.")

            return self.usuario_manager.add_role(cpf, role)

        except Exception as e:
            if config.DEBUG:
                print(f"Erro ao adicionar papel ao usuário: {str(e)}")
            return None

    def user_remove_role(self, cpf: str, role: str):
        try:
            if 'admin' not in USER_SESSION.get_user_data().roles:
                raise Exception("Necessário permissão de administrador.")

            return self.usuario_manager.remove_role(cpf, role)

        except Exception as e:
            if config.DEBUG:
                print(f"Erro ao remover papel do usuário: {str(e)}")
            return None

    def _validate_input(self, nome: str, sobrenome: str, cpf: str, nome_empresa: str, cargo: str, email: str, telefone: str, pais: str, senha: str, confirme_senha: str):
        if not Check.Nome(nome, sobrenome):
            raise NomeInvalido(nome, sobrenome)

        if not Check.Email(email):
            raise EmailInvalido(email)

        if not Check.Telefone(telefone):
            raise TelefoneInvalido(telefone)

        if not Check.Senha(senha, confirme_senha):
            raise SenhaInvalido()

        if not Check.CPF(cpf):
            raise CPFInvalido(cpf)

    def _validar_senha_atual(self, senha: str, cpf: str):
        senha_hash = senha
        if USER_SESSION.get_user_data().cpf != cpf:
            raise CPFInvalido(cpf)
        return USER_SESSION.get_user_data().senha == senha_hash

    def _calcular_sha256(self, texto: str):
        texto_codificado = texto.encode('utf-8')
        sha256_hash = hashlib.sha256(texto_codificado)
        return sha256_hash.hexdigest()
    
    def get_user_by_email_conselt(self, email,senha):
        self.conselt_manager.connect()
    
        usuario = self.conselt_manager.login(email)
        
        if usuario:
            if usuario.senha != senha:
                raise UsuarioOuSenhaInvalido()
            try:
                self.usuario_manager.create(usuario.nome, usuario.sobrenome, usuario.cpf, usuario.nomeEmpresa, usuario.cargo, usuario.email, usuario.telefone, usuario.pais, self._calcular_sha256(usuario.senha))
            except Exception as e:
                print(f"Erro ao criar usuário vindo da conselt: {str(e)}")
        else:
            print(f"Usuário '{email}' não encontrado.")

        self.conselt_manager.disconnect()
        return usuario
