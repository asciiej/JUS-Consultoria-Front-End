from src.utilitarios.operacoesDocumento import combine_dicts
class ContratoPseudoPreenchido:
    def __init__(self,titulo:str,informacoes:dict = None):
        self.titulo = titulo
        self.informacoes = informacoes

    def addInformacaoPseudo(self,informacoes:dict,parte:str=None):
        if not informacoes: return
        if parte: informacoes = {f"{parte}{chave}": valor for chave, valor in informacoes.items()}
        self.informacoes = combine_dicts(self.informacoes,informacoes)
    
    def printInformacaoPseudo(self):
        print("Nome do Contrato: ",self.titulo)
        if not self.informacoes: return
        for chave, valor in self.informacoes.items():
            print(f'"{chave}":"{valor}"')

    def getInformacaoPseudo(self,chave) -> str:
        if chave not in self.informacoes:
            return None
        return self.informacoes[chave]