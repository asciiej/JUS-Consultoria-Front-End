class empresaModel:

    def init(self,nome:str,cnpj:str,cnaePrincipal:str,cnaeSecundario:str,cfopPrincipaisProdutos:str,industriaSetor:str,receitaAnual:str):
        self.nome = nome
        self.cnpj = cnpj
        self.cnaePrincipal = cnaePrincipal
        self.cnaeSecundario = cnaeSecundario
        self.cfopPrincipaisProdutos = cfopPrincipaisProdutos
        self.industriaSetor = industriaSetor
        self.receitaAnual = receitaAnual

    def str(self)->str:
         return (f"Nome: {self.nome}\n"
                f"CNPJ: {self.cnpj}\n"
                f"CNAE Principal: {self.cnaeSecundario}\n"
                f"CNAE Secundario: {self.cnaePrincipal}\n"
                f"CFOP: {self.cfopPrincipaisProdutos}\n"
                f"Indústria Setor: {self.industriaSetor}\n"
                f"Receita Anual: {self.receitaAnual}")
