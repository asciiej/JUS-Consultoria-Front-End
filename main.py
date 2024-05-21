import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '.')))

# from src.interface.login import telaLogin
# from src.classes.usuario.usuarioControler import usuarioControler
# from src.classes.contrato.contract_management import contractManager

# usuarioControler().cadastro("Lucas","Sabbatini Janot Procópio","700.302.181-10","ASCII","Programador","lucas.exemplo@ufu.br","+55 12 34567-8901","Brasil","luc@s123","luc@s123")
# usuarioControler().login("lucas.exemplo@ufu.br","luc@s123")

# print(contractManager().listaContratos())