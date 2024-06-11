import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '.')))

from src.interface.login import telaLogin
from src.interface.Cadastro_Usuario.cadastroUsuarioo import telaCadastro
from src.interface.Atualizar_dados.atualizarinform import AtualizaCad

#telaLogin()
#telaCadastro()
AtualizaCad()