from src.interface.assinaturaDocumento import telaAssinaturaDocumento
import customtkinter as ctk
from PIL import Image
from ..utilitarios.user_session import USER_SESSION
from src.utilitarios.operacoesDocumento import convertPDF,combine_dicts



class checagemInformacoes(ctk.CTkFrame):
    def __init__(self,parent,controlers:dict):
       
        super().__init__(parent)
        self.parent = parent
        #self = janela
        self.font = ctk.CTkFont('Helvetica', 14)
        self.titulo_font = ctk.CTkFont('Helvetica', 20)

        self.framePrincipal = {
            "corner_radius": 30,
            "border_width": 2,
            "fg_color": ["#6EC1E4", "#6EC1E4"],
            "border_color": ["#00343D", "#00343D"]
        }

        # Cabeçalho menu personalizado
        self.cabecalho_menu = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#6EC1E4", "#6EC1E4"]
        }


    def show_contentCHECA(self, id ,titulo, tipo, controlers):
        print(f" '{titulo}' ")
        print(f" '{tipo}' ")
        print(f" '{id}' ")
        # Realiza a consulta ao banco de dados
        self.retornoBD = controlers['contract'].modeloDeContrato().get_by_title(titulo)
        self.camposPersonalizados = controlers['contract'].modeloDeContrato().get_campos_personalizados(titulo)
        self.tipo = tipo
        self.titulo = titulo
        
        if tipo == "Consultoria Tributária":
            self.contract = controlers['contract'].tributaria()
        elif tipo == "Câmara de Arbitragem":
            self.contract = controlers['contract'].arbitragem()
        elif tipo == "Consultoria Empresarial":
            self.contract = controlers['contract'].empresarial()   

        # Cabeçalho
        self.cabecalho = ctk.CTkFrame(self, height=104, **self.cabecalho_menu)
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

        self.nome_usuario_label = ctk.CTkLabel(self.cabecalho, text=f"{USER_SESSION.get_user_data().nome} {USER_SESSION.get_user_data().sobrenome}", font=self.font)
        self.nome_usuario_label.pack(side=ctk.RIGHT, padx=(0, 25))

        # Frame
        self.frame = ctk.CTkFrame(self,height=480,width=900,**self.framePrincipal)
        self.frame.pack(pady=(80, 0))

        self.buttonContinue = ctk.CTkButton(self, text="Prosseguir", command=self.prosseguir_funcao,height=30,width=300)
        self.buttonContinue.pack(side=ctk.TOP, pady=(30, 0),padx=(500,0))

        self.pagina = 0
        self.finalDict = None

        if tipo == "Consultoria Empresarial":
            self.informacoesContratante("Contratante")
        elif tipo == "Consultoria Tributária" or tipo == "Câmara de Arbitragem":
            #apenas informações empresariais
            self.informacoesEmpresariais()
        
        

    def prosseguir_funcao(self):
        if not self.camposPersonalizados:
            self.prosseguirSemInformacoesPersonalizadas()
            return
        if self.tipo == "Consultoria Tributária" or self.tipo == "Câmara de Arbitragem":
            match self.pagina:
                case 0:
                    retorno = self.get_informacoesEmpresariais()
                case 1:
                    retorno = self.get_informacoesPersonalizadas()
        elif self.tipo == "Consultoria Empresarial":
            match self.pagina:
                case 0:
                    retorno = self.get_informacoesContratado("Contratante")
                case 1:
                    retorno = self.get_informacoesContratado("Contratada")
                case 2:
                    retorno = self.get_informacoesNegocio()
                case 3:
                    retorno = self.get_informacoesPersonalizadas()

        self.finalDict = combine_dicts(self.finalDict,retorno)
        for widget in self.frame.winfo_children():
            widget.destroy()

        if self.tipo == "Consultoria Empresarial":
            match self.pagina:
                case 0:
                    self.informacoesContratante("Contratada")
                case 1:
                    self.informacoesNegocio()
                case 2:
                    self.informacoesPersonalizadas()
                case 3:
                    self.clear_check_screen()
                    self.contract.setContractData(self.finalDict)
                    self.formPdf()
                    
                   # self.unbind("<Configure>")
                    #for widget in self.winfo_children():
                     #   widget.destroy()
                    self.parent.show_frame("telaAssinaturaDocumento")
                    self.parent.frames["telaAssinaturaDocumento"].show_contentASSINA(id, self.titulo, self.tipo)

        else:
            match self.pagina:
                case 0:
                    self.informacoesPersonalizadas()
                case 1:
                    self.clear_check_screen()
                    self.contract.setContractData(self.finalDict)
                    self.formPdf()
                   # self.unbind("<Configure>")
                   # for widget in self.winfo_children():
                      #  widget.destroy()
                    self.parent.show_frame("telaAssinaturaDocumento")
                    self.parent.frames["telaAssinaturaDocumento"].show_contentASSINA(id, self.titulo, self.tipo)
        
        self.pagina +=1

    def prosseguirSemInformacoesPersonalizadas(self):
        if self.tipo == "Consultoria Tributária" or self.tipo == "Câmara de Arbitragem":
            retorno = self.get_informacoesEmpresariais()
        elif self.titulo == "Consultoria Empresarial":
            match self.pagina:
                case 0:
                    retorno = self.get_informacoesContratado("Contratante")
                case 1:
                    retorno = self.get_informacoesContratado("Contratada")
                case 2:
                    retorno = self.get_informacoesNegocio()

        self.finalDict = combine_dicts(self.finalDict,retorno)
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
                    self.contract.setContractData(self.finalDict)
                    self.formPdf()
                   # self.unbind("<Configure>")
                   # for widget in self.winfo_children():
                      #  widget.destroy()
                    self.parent.show_frame("telaAssinaturaDocumento")
                    self.parent.frames["telaAssinaturaDocumento"].show_contentASSINA(id, self.titulo, self.tipo)
            self.pagina +=1   
        else:
            self.clear_check_screen()
            self.contract.setContractData(self.finalDict)
            self.formPdf()
            #self.unbind("<Configure>")
            #for widget in self.winfo_children():
             #    widget.destroy()   
            self.parent.show_frame("telaAssinaturaDocumento")
            self.parent.frames["telaAssinaturaDocumento"].show_contentASSINA(id, self.titulo, self.tipo)

    def formPdf(self):
        pdf_saida = './pdfs/pdf_final.pdf'
        papel_timbrado = './pdfs/papelTimbrado.pdf'
        pdf_com_texto = './pdfs/output.pdf'
        try:
            translateDict = self.contract.getTranslateDict()
            convertPDF(self.retornoBD, papel_timbrado, pdf_com_texto, pdf_saida,translateDict).run()
        except Exception as e:
            print("Excessão na abertura do arquivo: ",e)
    
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

        self.Qualificacao = ctk.CTkLabel(self.frame, text="Qualificação da Parte",fg_color="#6EC1E4")
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

    def informacoesPersonalizadas(self):
        self.frame.destroy()
        self.buttonContinue.destroy()
        self.frame = ctk.CTkScrollableFrame(self,height=400,width=900,**self.framePrincipal)
        self.frame.pack(pady=(80, 0))

        self.buttonContinue = ctk.CTkButton(self, text="Prosseguir", command=self.prosseguir_funcao,height=30,width=300)
        self.buttonContinue.pack(side=ctk.TOP, pady=(30, 0),padx=(500,0))

        self.tituloInformacoesPersonalizadas = ctk.CTkLabel(self.frame, text="Informações Adicionais",fg_color="#6EC1E4",font =('Helvetica', 24))
        self.tituloInformacoesPersonalizadas.pack(padx=30, pady=(20,40),anchor="w")

        self.camposPersonalizadosEntry = []
        for i,campo in enumerate(self.camposPersonalizados):
            print(i)
            self.camposPersonalizadosLable = ctk.CTkLabel(self.frame, text=campo,fg_color="#6EC1E4")
            self.camposPersonalizadosLable.pack(padx=(280,0),pady=5,anchor="w")

            self.camposPersonalizadosEntry.append(ctk.CTkEntry(self.frame,height=30,width=400))
            self.camposPersonalizadosEntry[i].pack(padx=(40,20), pady=(0,30))

    def get_informacoesNegocio(self):
        contract_data = {
		'valor': self.ValorEntry.get(),
		'forma_pagamento': self.FormaPagamentoEntry.get(),
		'multa_mora': self.MultaDeMoraEntry.get(),
		'juros_mora': self.JurosDeMoraEntry.get(),
		'correcao_monetaria': self.CorrecaoMonetariaEntry.get(),
		'prazo_duracao': self.PrazoDuracaoEntry.get(),
		'contratante': self.contratante_data,
		'contratado': self.contratado_data
	    }
        return contract_data
    
    def get_informacoesEmpresariais(self):
        dictInformacoesEmpresariais = {
            'nome_empresa': self.NomeEntry.get(),
            'cnpj': self.CnpjEntry.get(),
            'cnae_principal': self.Cnae1Entry.get(), 
            'cnae_secundaria': self.Cnae2Entry.get(), 
            'cfop_principais': self.CfopEntry.get(), 
            'industria_setor': self.IndustriaSetorEntry.get(),
            'receita_anual': self.ReceitaAnualEntry.get()
        }
        return dictInformacoesEmpresariais
    
    def get_informacoesContratado(self,contratante):
        if contratante == "Contratante":
            self.contratante_data = {
                'nome': self.NomeContractEntry.get(),
                'nacionalidade': self.NacionalidadeEntry.get(),
                'estadocivil': self.EstadoCivilEntry.get(),
                'cpf': self.CpfOuCnpjEntry.get(),
                'profissao': self.ProfissaoEntry.get(),
                'endereco': self.EnderecoEntry.get()
            }
            return None
        elif contratante == "Contratada":
            self.contratado_data = {
                'nome': self.NomeContractEntry.get(),
                'nacionalidade': self.NacionalidadeEntry.get(),
                'estadocivil': self.EstadoCivilEntry.get(),
                'cpf': self.CpfOuCnpjEntry.get(),
                'profissao': self.ProfissaoEntry.get(),
                'endereco': self.EnderecoEntry.get()
            }
            return None

    def get_informacoesPersonalizadas(self):
        for i,entrada in enumerate(self.camposPersonalizadosEntry):
            self.camposPersonalizadosEntry[i] = entrada.get()

        dictInformacoes = {chave : valor for chave,valor in zip(self.camposPersonalizados,self.camposPersonalizadosEntry)}
        print(dictInformacoes)
        return {"informacoes_personalizadas" : dictInformacoes}
    
    def voltar_funcao(self):
        self.unbind("<Configure>")
        for widget in self.winfo_children():
            widget.destroy()
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