from src.interface.assinaturaDocumento import telaAssinaturaDocumento
import tkinter
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from ..utilitarios.user_session import USER_SESSION
from functools import partial


class checagemInformacoes(ctk.CTkFrame):
    def __init__(self,parent,controlers:dict):
       
        super().__init__(parent)
        self.parent = parent
        
        self.retornoBD = controlers['contract']
        
            
        ctk.set_default_color_theme("lib/temaTkinterCustom.json")

        #self = janela
        self.font = ctk.CTkFont('Helvetica', 14)
        self.titulo_font = ctk.CTkFont('Helvetica', 20)

        # Cabeçalho menu personalizado
        cabecalho_menu = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#6EC1E4", "#6EC1E4"]
        }

        # Cabeçalho
        self.cabecalho = ctk.CTkFrame(self, height=104, **cabecalho_menu)
        self.cabecalho.pack(fill=ctk.X)

        # Logo
        self.logoJUS = ctk.CTkImage(Image.open('imagens/Logomarca JUS.png'), size=(80, 72.54))
        self.logo_cabecalho = ctk.CTkLabel(self.cabecalho, image=self.logoJUS, text="")
        self.logo_cabecalho.pack(side=ctk.LEFT, padx=(18, 0), pady=7)

        # Usuario foto
        self.userPic = ctk.CTkImage(Image.open('imagens/User Male Black.png'), size=(90, 90))
        self.userPic_cabecalho = ctk.CTkLabel(self.cabecalho, image=self.userPic, text="")
        self.userPic_cabecalho.pack(side=ctk.RIGHT, padx=(0, 18), pady=7)

        # Botão menu personalizado
        voltar_menu = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#6EC1E4", "#6EC1E4"],
            "hover_color": ["#6EC1E4", "#6EC1E4"],
            "border_color": ["#6EC1E4", "#6EC1E4"],
            "text_color": "#000000",
            "text_color_disabled": ["#6EC1E4", "#6EC1E4"]
        }

        # Texto menu e Botão de VOLTAR
        self.h1_titulo = ctk.CTkLabel(self.cabecalho, text="Preencha suas informações", font=self.titulo_font)
        self.h1_titulo.pack(side=ctk.LEFT, padx=(25, 0))

        self.voltar = ctk.CTkButton(self.cabecalho, text="Voltar \u2192", command=self.voltar_funcao,height=30, **voltar_menu)
        self.voltar.pack(side=ctk.LEFT, padx=(700, 0))

        
        self.buttonContinue = ctk.CTkButton(self, text="Prosseguir", command=self.prosseguir_funcao,height=30,width=300)
        self.buttonContinue.pack(side=ctk.TOP, pady=(30, 0),padx=(500,0))

    def show_contentCHECA(self, id, tipo, titulo, controlers):
            print(f" '{titulo}' ")
            print(f" '{tipo}' ")
            # Realiza a consulta ao banco de dados
            self.retornoBD = controlers['contract'].modeloDeContrato().get_by_title(tipo)
            self.tipo = tipo
            self.titulo = titulo
            

            # Nome do usuario no cabeçalho
            #       self.nome_usuario_label = ctk.CTkLabel(self.cabecalho, text="Lucas Simoni", font=self.font)
            self.nome_usuario_label = ctk.CTkLabel(self.cabecalho, text=f"{USER_SESSION.get_user_data().nome} {USER_SESSION.get_user_data().sobrenome}", font=self.font)
            self.nome_usuario_label.pack(side=ctk.RIGHT, padx=(0, 25))

            # Frame
            self.frame = ctk.CTkFrame(self,height=480,width=900)
            self.frame.pack(pady=(80, 0))

            self.pagina = 0
            self.finalDict = None

            if titulo == "Consultoria Empresarial":
                self.informacoesContratante("Contratante")
            elif titulo == "Consultoria Tributária" or titulo == "Câmara de Arbitragem":
                #apenas informações empresariais
                self.informacoesEmpresariais()
        
        

    def prosseguir_funcao(self):
        if self.titulo == "Consultoria Tributária" or self.titulo == "Câmara de Arbitragem":
            retorno = self.get_informacoesEmpresariais()
        elif self.titulo == "Consultoria Empresarial":
            match self.pagina:
                case 0:
                    retorno = self.get_informacoesContratado("Contratante")
                case 1:
                    retorno = self.get_informacoesContratado("Contratada")
                case 2:
                    retorno = self.get_informacoesNegocio()

        self.finalDict = self.combine_dicts(self.finalDict,retorno)
        for widget in self.frame.winfo_children():
            widget.destroy()

        if self.titulo == "Consultoria Empresarial":
            match self.pagina:
                case 0:
                    self.informacoesContratante("Contratada")
                case 1:
                    self.informacoesNegocio()
                case 2:
                    self.clear_check_screen()
                    telaAssinaturaDocumento(self,self.controlers,self.finalDict)
            self.pagina +=1
        else:
            self.clear_check_screen()
            telaAssinaturaDocumento(self,self.controlers,self.finalDict)
    
    def clear_check_screen(self):
        """Função para limpar a tela de login."""
        # Remove todos os widgets do root
        for widget in self.winfo_children():
            widget.destroy()

    def informacoesEmpresariais(self):
        # Label dentro do frame filho
        TitleLable = ctk.CTkLabel(self.frame,text="Informações Empresariais",fg_color="#6EC1E4",font =('Helvetica', 24))
        TitleLable.grid(row = 0,column = 0,padx=30, pady=40)

        self.frame.grid_columnconfigure(1, minsize=100)
        self.frame.grid_columnconfigure(2, minsize=100)
        self.frame.grid_columnconfigure(3, minsize=100)
        self.frame.grid_columnconfigure(4, minsize=300)

        self.Nome = ctk.CTkLabel(self.frame, text="Nome da Empresa",fg_color="#6EC1E4")
        self.Nome.grid(row=1, column=0, padx=50, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.NomeEntry = ctk.CTkEntry(self.frame,height=30)
        self.NomeEntry.grid(row=2, column=0, columnspan=4, padx=(40,20), pady=(0,30),sticky="ew")

        self.Cnpj = ctk.CTkLabel(self.frame, text="CNPJ",fg_color="#6EC1E4")
        self.Cnpj.grid(row=1, column=4, padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.CnpjEntry = ctk.CTkEntry(self.frame,height=30)
        self.CnpjEntry.grid(row=2, column=4, columnspan=3, padx=(20,40), pady=(0,30),sticky="ew")

        self.Cnae1 = ctk.CTkLabel(self.frame, text="CNAE Principal",fg_color="#6EC1E4")
        self.Cnae1.grid(row=3, column=0,padx=50, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.Cnae1Entry = ctk.CTkEntry(self.frame,height=30)
        self.Cnae1Entry.grid(row=4, column=0, columnspan=2, padx=(40,20), pady=(0,30),sticky="ew") 

        self.Cnae2 = ctk.CTkLabel(self.frame, text="CNAE Secundário",fg_color="#6EC1E4")
        self.Cnae2.grid(row=3, column=2, padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.Cnae2Entry = ctk.CTkEntry(self.frame,height=30)
        self.Cnae2Entry.grid(row=4, column=2, columnspan=2, padx=20, pady=(0,30),sticky="ew") 

        self.Cfop = ctk.CTkLabel(self.frame, text="CFOP Principais Produtos",fg_color="#6EC1E4")
        self.Cfop.grid(row=3, column=4, padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.CfopEntry = ctk.CTkEntry(self.frame,height=30)
        self.CfopEntry.grid(row=4, column=4, columnspan=3, padx=(20,40), pady=(0,30),sticky="ew") 

        self.IndustriaSetor = ctk.CTkLabel(self.frame, text="Indústria/Setor",fg_color="#6EC1E4")
        self.IndustriaSetor.grid(row=5,column = 0, padx=50, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.IndustriaSetorEntry = ctk.CTkEntry(self.frame,height=30)
        self.IndustriaSetorEntry.grid(row=6, column=0, columnspan=2, padx=(40,20), pady=(0,30),sticky="ew")

        self.ReceitaAnual = ctk.CTkLabel(self.frame, text="Receita Anual",fg_color="#6EC1E4")
        self.ReceitaAnual.grid(row=5,column=2,padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.ReceitaAnualEntry = ctk.CTkEntry(self.frame,height=30)
        self.ReceitaAnualEntry.grid(row=6, column=2, columnspan=2, padx=20, pady=(0,30),sticky="ew")



    def informacoesContratante(self,parte:str):
        # Label dentro do frame filho
        if parte == "Contratante":
            text = "Informações do Contratante"
        elif parte == "Contratada":
            text = "Informações da Contratada"

        TitleLable = ctk.CTkLabel(self.frame,text=text,fg_color="#6EC1E4",font =('Helvetica', 24))
        TitleLable.grid(row = 0,column = 0,padx=30, pady=40)

        self.frame.grid_columnconfigure(1, minsize=100)
        self.frame.grid_columnconfigure(2, minsize=100)
        self.frame.grid_columnconfigure(3, minsize=100)
        self.frame.grid_columnconfigure(4, minsize=300)

        self.Nome = ctk.CTkLabel(self.frame, text="Nome Completo",fg_color="#6EC1E4")
        self.Nome.grid(row=1, column=0, padx=50, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.NomeContractEntry = ctk.CTkEntry(self.frame,height=30)
        self.NomeContractEntry.grid(row=2, column=0, columnspan=4, padx=(40,20), pady=(0,30),sticky="ew")

        self.Nacionalidade = ctk.CTkLabel(self.frame, text="Nacionalidade",fg_color="#6EC1E4")
        self.Nacionalidade.grid(row=1, column=4, padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.NacionalidadeEntry = ctk.CTkEntry(self.frame,height=30)
        self.NacionalidadeEntry.grid(row=2, column=4, columnspan=3, padx=(20,40), pady=(0,30),sticky="ew")

        self.EstadoCivil = ctk.CTkLabel(self.frame, text="Estado Civil",fg_color="#6EC1E4")
        self.EstadoCivil.grid(row=3, column=0,padx=50, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.EstadoCivilEntry = ctk.CTkEntry(self.frame,height=30)
        self.EstadoCivilEntry.grid(row=4, column=0, columnspan=2, padx=(40,20), pady=(0,30),sticky="ew") 

        self.Profissao = ctk.CTkLabel(self.frame, text="Profissão",fg_color="#6EC1E4")
        self.Profissao.grid(row=3, column=2, padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.ProfissaoEntry = ctk.CTkEntry(self.frame,height=30)
        self.ProfissaoEntry.grid(row=4, column=2, columnspan=2, padx=20, pady=(0,30),sticky="ew") 

        self.CpfOuCnpj = ctk.CTkLabel(self.frame, text="CPF ou CNPJ",fg_color="#6EC1E4")
        self.CpfOuCnpj.grid(row=3, column=4, padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.CpfOuCnpjEntry = ctk.CTkEntry(self.frame,height=30)
        self.CpfOuCnpjEntry.grid(row=4, column=4, columnspan=3, padx=(20,40), pady=(0,30),sticky="ew") 

        self.Endereco = ctk.CTkLabel(self.frame, text="Endereço de Residência ou Comercial",fg_color="#6EC1E4")
        self.Endereco.grid(row=5,column = 0, padx=50, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.EnderecoEntry = ctk.CTkEntry(self.frame,height=30)
        self.EnderecoEntry.grid(row=6, column=0, columnspan=2, padx=(40,20), pady=(0,30),sticky="ew")

        self.Qualificacao = ctk.CTkLabel(self.frame, text="Qualificação das Partes",fg_color="#6EC1E4")
        self.Qualificacao.grid(row=5,column=2,padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.QualificacaoEntry = ctk.CTkEntry(self.frame,height=30)
        self.QualificacaoEntry.grid(row=6, column=2, columnspan=2, padx=20, pady=(0,30),sticky="ew")

    
    def informacoesNegocio(self):
        # Label dentro do frame filho
        TitleLable = ctk.CTkLabel(self.frame,text="Informações do Negócio",fg_color="#6EC1E4",font =('Helvetica', 24))
        TitleLable.grid(row = 0,column = 0,padx=30, pady=40)

        self.frame.grid_columnconfigure(1, minsize=100)
        self.frame.grid_columnconfigure(2, minsize=100)
        self.frame.grid_columnconfigure(3, minsize=100)
        self.frame.grid_columnconfigure(4, minsize=300)

        self.Valor = ctk.CTkLabel(self.frame, text="Valor",fg_color="#6EC1E4")
        self.Valor.grid(row=1, column=0, padx=50, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.ValorEntry = ctk.CTkEntry(self.frame,height=30)
        self.ValorEntry.grid(row=2, column=0, columnspan=4, padx=(40,20), pady=(0,30),sticky="ew")

        self.FormaPagamento = ctk.CTkLabel(self.frame, text="Forma de Pagamento",fg_color="#6EC1E4")
        self.FormaPagamento.grid(row=1, column=4, padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.FormaPagamentoEntry = ctk.CTkEntry(self.frame,height=30)
        self.FormaPagamentoEntry.grid(row=2, column=4, columnspan=3, padx=(20,40), pady=(0,30),sticky="ew")

        self.MultaDeMora = ctk.CTkLabel(self.frame, text="Multa de Mora",fg_color="#6EC1E4")
        self.MultaDeMora.grid(row=3, column=0,padx=50, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.MultaDeMoraEntry = ctk.CTkEntry(self.frame,height=30)
        self.MultaDeMoraEntry.grid(row=4, column=0, columnspan=2, padx=(40,20), pady=(0,30),sticky="ew") 

        self.JurosDeMora = ctk.CTkLabel(self.frame, text="Juros de Mora",fg_color="#6EC1E4")
        self.JurosDeMora.grid(row=3, column=2, padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.JurosDeMoraEntry = ctk.CTkEntry(self.frame,height=30)
        self.JurosDeMoraEntry.grid(row=4, column=2, columnspan=2, padx=20, pady=(0,30),sticky="ew") 

        self.CorrecaoMonetaria = ctk.CTkLabel(self.frame, text="Correção Monetária",fg_color="#6EC1E4")
        self.CorrecaoMonetaria.grid(row=3, column=4, padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.CorrecaoMonetariaEntry = ctk.CTkEntry(self.frame,height=30)
        self.CorrecaoMonetariaEntry.grid(row=4, column=4, columnspan=3, padx=(20,40), pady=(0,30),sticky="ew") 

        self.PrazoDuracao = ctk.CTkLabel(self.frame, text="Prazo de Duração",fg_color="#6EC1E4")
        self.PrazoDuracao.grid(row=5,column = 0, padx=50, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.PrazoDuracaoEntry = ctk.CTkEntry(self.frame,height=30)
        self.PrazoDuracaoEntry.grid(row=6, column=0, columnspan=2, padx=(40,20), pady=(0,30),sticky="ew")


    def get_informacoesNegocio(self):
        dictInformacoesDoNegocio = {
            "$$valor$$": self.ValorEntry.get(),
            "$$formadepagamento$$": self.FormaPagamentoEntry.get(),
            "$$multademora$$": self.MultaDeMoraEntry.get(),
            "$$jurosdemora$$": self.JurosDeMoraEntry.get(),
            "$$correçãomonetária$$": self.CorrecaoMonetariaEntry.get(),
            "$$prazodeduração$$": self.PrazoDuracaoEntry.get(),
        }
        return dictInformacoesDoNegocio
    
    def get_informacoesEmpresariais(self):
        dictInformacoesEmpresariais = {
            "$$nomedaempresa$$": self.NomeEntry.get(),
            "$$cnpj$$": self.CnpjEntry.get(),
            "$$cnaeprincipal$$": self.Cnae1Entry.get(),
            "$$cnaesecundário$$": self.Cnae2Entry.get(),
            "$$cfopprincipaisprodutos$$": self.CfopEntry.get(),
            "$$indústria/setor$$": self.IndustriaSetorEntry.get(),
            "$$receitaanual$$": self.ReceitaAnualEntry.get(),
        }
        return dictInformacoesEmpresariais
    
    def get_informacoesContratado(self,contratante):
        if contratante == "Contratante":
            dictContratante = {            
            "$$nomecompletocontratante$$": self.NomeContractEntry.get(),
            "$$nacionalidadecontratante$$": self.NacionalidadeEntry.get(),
            "$$estadocivilcontratante$$": self.EstadoCivilEntry.get(),
            "$$profissãocontratante$$": self.ProfissaoEntry.get(),
            "$$cpfoucnpjcontratante$$": self.CpfOuCnpjEntry.get(),
            "$$endereçoresidêncial/comercialcontratante$$":self.EnderecoEntry.get(),
        }
            return dictContratante
        elif contratante == "Contratada":
            dictContratado = {
            "$$nomecompletocontratado$$": self.NomeContractEntry.get(),
            "$$nacionalidadecontratado$$": self.NacionalidadeEntry.get(),
            "$$estadocivilcontratado$$": self.EstadoCivilEntry.get(),
            "$$profissãocontratado$$": self.ProfissaoEntry.get(),
            "$$cpfoucnpjcontratado$$": self.CpfOuCnpjEntry.get(),
            "$$endereçoresidêncial/comercialcontratado$$": self.EnderecoEntry.get(),
        }
            return dictContratado
    
    def combine_dicts(self,dict1, dict2):
        # Verifica se o primeiro dicionário é nulo
        if dict1 is None:
            # Retorna uma cópia do segundo dicionário se o primeiro for nulo
            return dict(dict2) if dict2 else {}

        # Verifica se o segundo dicionário é nulo
        if dict2 is None:
            # Retorna uma cópia do primeiro dicionário se o segundo for nulo
            return dict(dict1)

        # Cria um terceiro dicionário combinando os dois
        combined_dict = dict(dict1)  # Cria uma cópia do primeiro dicionário
        combined_dict.update(dict2)  # Atualiza com os valores do segundo dicionário

        return combined_dict

    def voltar_funcao(self):
        self.parent.show_frame("telaPrincipal")
        self.parent.frames["telaPrincipal"].show_content()







# dictUser = {
#             "$$nome$$": ,
#             "$$sobrenome$$": ,
#             "$$cpf$$": ,
#             "$$empresa$$": ,
#             "$$cargo$$": ,
#             "$$email$$": ,
#             "$$telefone$$": ,
#             "$$país/localização$$": ,
#         }    