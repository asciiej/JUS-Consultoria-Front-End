from ...utilitarios.excecoes import UsuarioOuSenhaInvalido
import config
class UsuarioModel:
	def __init__(self, nome: str, sobrenome: str, cpf:str, nomeEmpresa:str, cargo:str, email: str, telefone: str, pais: str, senha:str, roles:tuple):
		self.nome = nome
		self.sobrenome = sobrenome
		self.cpf = cpf
		self.nomeEmpresa = nomeEmpresa
		self.cargo = cargo
		self.email = email
		self.telefone = telefone
		self.pais = pais
		self.senha = senha
		self.roles = roles

	def str(self) -> str:
		return (f"Nome: {self.nome} {self.sobrenome}\n"
				f"CPF: {self.cpf}\n"
				f"Nome da Empresa: {self.nomeEmpresa if self.nomeEmpresa is not None else 'Não informado'}\n"
				f"Cargo: {self.cargo if self.cargo is not None else 'Não informado'}\n"
				f"E-mail: {self.email}\n"
				f"Telefone: {self.telefone}\n"
				f"Roles: {self.roles}\n"
				f"País/Localização: {self.pais}")
	
	def getTranslateDict(self):
		dictUser = {
            "$$nome$$": self.nome,
            "$$sobrenome$$": self.sobrenome,
            "$$cpf$$": self.cpf,
            "$$empresa$$": self.nomeEmpresa,
            "$$cargo$$": self.cargo,
            "$$email$$": self.email,
            "$$telefone$$": self.telefone,
            "$$país/localização$$": self.pais,
        }
		return dictUser


# TODO: Tratar erros em todos os metodos
class UsuarioManager:
	def __init__(self, db):
		self.db = db

	def login(self, email, senha):
		try:
			usuario = self.get_by_email(email)
		except Exception as e:
			print(f"Erro ao buscar usuário por email {email}: {str(e)}")
			return None  # Propaga a exceção para cima, se necessário

		if usuario is None:
			raise UsuarioOuSenhaInvalido()

		if usuario.senha != senha:
			raise UsuarioOuSenhaInvalido()

		return usuario

	# (2, 'Carlos', 'Santos', '987.654.321-00', 'SimCorp', 'Engenheiro de Cozinha', 'carlos.santos@example.com', '+55 12 34567-8901', 'EUA', '07cd109ac902429f267f8279f2a0041c')

	def create(self, nome: str, sobrenome: str, cpf: str, nomeEmpresa: str, cargo: str, email: str, telefone: str, pais: str, senha: str):
		try:
			if self.get_by_cpf(cpf) is not None:
				raise Exception(f"CPF {cpf} ja existe")

			query = """
				INSERT INTO users.clients (nome, sobrenome, cpf, nome_empresa, cargo, email, telefone, pais, senha)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
				RETURNING nome, sobrenome, cpf, nome_empresa, cargo, email, telefone, pais, senha, roles;
				"""
			params = (nome, sobrenome, cpf, nomeEmpresa, cargo, email, telefone, pais, senha)

			result = self.db.query(query, params)
			if result:
				return UsuarioModel(
					nome=result[1], sobrenome=result[2], cpf=result[3],
					nomeEmpresa=result[4], cargo=result[5], email=result[6],
					telefone=result[7], pais=result[8], senha=result[9],roles=result[10]
				)

		except Exception as e:
			print(f"Erro ao criar usuário: {str(e)}")
			return None

		return None

	def get_all(self):
		try:
			query = "SELECT * FROM users.clients"
			result = self.db.query(query)
			if len(result) == 0:
				raise Exception('Nenhum registro encontrado')

			return [
				UsuarioModel(
					nome=row[1], sobrenome=row[2], cpf=row[3],
					nomeEmpresa=row[4], cargo=row[5], email=row[6],
					telefone=row[7], pais=row[8], senha=row[9], roles=row[10]
				) for row in result
			]

		except Exception as e:
			print(f"Erro ao buscar todos os usuários: {str(e)}")
			return None

	def get_by_cpf(self, cpf: str):
		try:
			query = "SELECT * FROM users.clients WHERE cpf = %s"
			resultDB = self.db.query(query, (cpf,))

			if resultDB and len(resultDB) > 0:
				result = resultDB[0]
				return UsuarioModel(
					nome=result[1], sobrenome=result[2], cpf=result[3],
					nomeEmpresa=result[4], cargo=result[5], email=result[6],
					telefone=result[7], pais=result[8], senha=result[9], roles=result[10]
				)

		except IndexError:
			print(f"Índice fora dos limites ao buscar por CPF {cpf}")
			return None

		except Exception as e:
			print(f"Erro ao buscar usuário por CPF {cpf}: {str(e)}")
			return None

	def get_by_email(self, email: str):
		try:
			query = "SELECT * FROM users.clients WHERE email = %s"
			resultDB = self.db.query(query, (email,))

			if resultDB and len(resultDB) > 0:
				result = resultDB[0]
				return UsuarioModel(
					nome=result[1], sobrenome=result[2], cpf=result[3],
					nomeEmpresa=result[4], cargo=result[5], email=result[6],
					telefone=result[7], pais=result[8], senha=result[9], roles=result[10]
				)

		except IndexError:
			print(f"Índice fora dos limites ao buscar por email {email}")
			return None

		except Exception as e:
			print(f"Erro ao buscar usuário por email {email}: {str(e)}")
			return None

	def get_roles(self, cpf: str):
		user = self.get_by_cpf(cpf)
		if user:
			return user.roles
		return None  # Ou pode levantar uma exceção se preferir

	def has_role(self, cpf: str, role: str):
		user = self.get_by_cpf(cpf)
		if user:
			return role in user.roles
		return False

	def add_role(self, cpf: str, role: str):
		user = self.get_by_cpf(cpf)

		if user:
			if role not in user.roles:
				query = """
					UPDATE users.clients
					SET roles = array_append(roles, %s)
					WHERE cpf = %s
					"""
				params = (role, cpf)
				self.db.query(query, params)

		return self.get_by_cpf(cpf)

	def remove_role(self, cpf: str, role: str):
		user = self.get_by_cpf(cpf)

		if user:
			if role in user.roles:
				query = """
					UPDATE users.clients
					SET roles = array_remove(roles, %s)
					WHERE cpf = %s
					"""
				params = (role, cpf)
				self.db.query(query, params)

		return self.get_by_cpf(cpf)


	def update(self, cpf: str, nome: str, sobrenome: str, nomeEmpresa: str, cargo: str, email: str, telefone: str, pais: str, senha: str):
		user = self.get_by_cpf(cpf)

		if user:
			query = """
				UPDATE users.clients
				SET nome = %s,
					sobrenome = %s,
					nome_empresa = %s,
					cargo = %s,
					email = %s,
					telefone = %s,
					pais = %s,
					senha = %s
				WHERE cpf = %s
				"""
			params = (nome, sobrenome, nomeEmpresa, cargo, email, telefone, pais, senha, cpf)

			try:
				self.db.query(query, params)
			except Exception as e:
				if config.DEBUG:
					print(f"Erro ao atualizar usuário com CPF {cpf}: {str(e)}")
				return None

		return self.get_by_cpf(cpf)

	def delete(self, cpf: str):
		user = self.get_by_cpf(cpf)

		if user:
			query = "DELETE FROM users.clients WHERE cpf = %s"

			try:
				self.db.query(query, (cpf,))
			except Exception as e:
				if config.DEBUG:
					print(f"Erro ao excluir usuário com CPF {cpf}: {str(e)}")
					return None

		return user