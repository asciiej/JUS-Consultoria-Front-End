from src.interface.assinaturaDocumento import telaAssinaturaDocumento

class checagemInformacoes():
    def __init__(self,id:int,tipo:str,título:str,controlers:dict):
        retornoBD = controlers['contract'].modeloDeContrato().get_by_title(título)
        print(retornoBD)

        if tipo == "Consultoria Empresarial":
            self.consultoria_empresarial()
        elif tipo == "Consultoria Tributária":
            self.consultoria_tributaria()
        elif tipo == "Câmara de Arbitragem":
            self.camara_arbitragem()

        #telaAssinaturaDocumento

    def consultoria_empresarial(self):
        print("Checando dados empresarial")
    def consultoria_tributaria(self):
        print("Checando dados tributaria")
    def camara_arbitragem(self):
        print("Checando dados arbitragem")