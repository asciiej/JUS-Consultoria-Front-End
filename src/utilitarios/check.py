import validate_cpf
import re

class Check:
    def Nome(nome:str,sobrenome:str):
        # Expressão regular para validar nomes com letras maiúsculas e minúsculas e acentos
        padraoNome = r'^[A-Za-zÀ-ÅÈ-ËÍ-ÏÐ-ÖØ-öø-ÿ]+$'

        # Expressão regular para validar nomes com letras maiúsculas e minúsculas, acentos e espaços
        padraoSobrenome = r'^[A-Za-zÀ-ÅÈ-ËÍ-ÏÐ-ÖØ-öø-ÿ\s]+$'

        if re.match(padraoNome, nome) and re.match(padraoSobrenome,sobrenome):
            return True
        else:
            return False

    def EMail(eMail:str):
        # Expressão regular para verificar endereços de e-mail
        padraoEMail = r'^[\w\-.]+@(?:[a-zA-Z0-9]+\.)+[a-zA-Z]{2,}$'
        if re.match(padraoEMail, eMail):
            return True
        else:
            return False

    def Telefone(telefone:str):
        padraoTelefone = r'^\+\d{2}\s\d{2}\s\d{5}-\d{4}$'

        if re.match(padraoTelefone, telefone):
            return True
        else:
            return False

    def String(cargo:str):
        padraoCargo = r'^[A-Za-zÀ-ÅÈ-ËÍ-ÏÐ-ÖØ-öø-ÿ\s]+$'
        if re.match(padraoCargo, cargo):
            return True
        else:
            return False

    def Senha(senha,confirmeSenha):
        return senha==confirmeSenha and ' ' not in senha

    def CPF(cpf):
        padraoCPF = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        if re.match(padraoCPF, cpf) and validate_cpf.is_valid(cpf):
            return True
        else:
            return False