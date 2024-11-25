from functools import partial
from src.utilitarios.excecoes import ContratoNaoEncontrado
import customtkinter as ctk
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, Toplevel, Label, Menu, ttk
from PIL import Image, ImageTk
from ..utilitarios.user_session import USER_SESSION
from src.utilitarios.operacoesDocumento import convertPDF,combine_dicts
from src.classes.contrato.ContratoPesudoPreenchido import ContratoPseudoPreenchido
from pathlib import Path
import os
import re


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
        # Realiza a consulta ao banco de dados
        contratoNaoEncontrado = False
        try:
            self.retornoBD = controlers['contract'].modeloDeContrato().get_by_title(titulo)
            self.camposPersonalizados = controlers['contract'].modeloDeContrato().get_campos_personalizados(titulo)
        except ContratoNaoEncontrado:
            contratoNaoEncontrado = True
        self.tipo = tipo
        self.titulo = titulo

        if tipo == "Consultoria Tributária":
            self.contract = controlers['contract'].tributaria()
        elif tipo == "Câmara de Arbitragem":
            self.contract = controlers['contract'].arbitragem()
        elif tipo == "Consultoria Empresarial":
            self.contract = controlers['contract'].empresarial()

        self.parent.setContrato(self.contract)
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


        self.nome_usuario_label = ctk.CTkLabel(self.cabecalho, text=f"{USER_SESSION.get_user_data().nome} {USER_SESSION.get_user_data().sobrenome}", font=self.font)
        self.nome_usuario_label.pack(side=ctk.RIGHT, padx=(0, 25))

        self.frameScroll = ctk.CTkScrollableFrame(self)
        self.frameScroll.pack(fill="both", expand=True)

        # Frame
        self.frame = ctk.CTkFrame(self.frameScroll,height=480,width=900,**self.framePrincipal)
        self.frame.pack(pady=(80, 0))

        # Frame para agrupar os botões
        self.button_frame = ctk.CTkFrame(self.frameScroll)
        self.button_frame.pack(pady=(30, 0), padx=(500, 0))

        # Botão Voltar
        self.voltar = ctk.CTkButton(self.button_frame, text="Voltar", command=partial(self.voltar_funcao, contratoNaoEncontrado), height=30)
        self.voltar.pack(padx=10,side=ctk.LEFT)

        # Botão Prosseguir
        self.buttonContinue = ctk.CTkButton(self.button_frame, text="Prosseguir", command=self.prosseguir_funcao, height=30, width=300)
        self.buttonContinue.pack(side=ctk.LEFT, padx=(0, 10))

        self.pagina = 0
        self.finalDict = None

        if contratoNaoEncontrado:
            self.contratoNaoEncontrado()
            return

        self.contratoPseudoPreenchido = self.parent.getContratoPseudoPreenchido(titulo)
        if  not self.contratoPseudoPreenchido:
            self.contratoPseudoPreenchido = ContratoPseudoPreenchido(titulo)

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
                    if not self.erroTodosOsCampos(self.get_informacoesEmpresariais()): return
                    retorno = self.get_informacoesEmpresariais()
                case 1:
                    if not self.erroTodosOsCampos(self.get_informacoesPersonalizadas()): return
                    retorno = self.get_informacoesPersonalizadas()
        elif self.tipo == "Consultoria Empresarial":
            match self.pagina:
                case 0:
                    if not self.erroTodosOsCampos(self.get_informacoesContratado("Contratante")): return
                    self.contratoPseudoPreenchido.addInformacaoPseudo(self.get_informacoesContratado("Contratante"),"Contratante")
                    retorno = None
                case 1:
                    if not self.erroTodosOsCampos(self.get_informacoesContratado("Contratada")): return
                    self.contratoPseudoPreenchido.addInformacaoPseudo(self.get_informacoesContratado("Contratada"),"Contratada")
                    retorno = None
                case 2:
                    if not self.erroTodosOsCampos(self.get_informacoesNegocio()): return
                    retorno = self.get_informacoesNegocio()
                case 3:
                    if not self.erroTodosOsCampos(self.get_informacoesPersonalizadas()): return
                    retorno = self.get_informacoesPersonalizadas()
        
        retornoContratoPseudoPreenchido = retorno            
        if retorno and 'informacoes_personalizadas' in retorno.keys():
            retornoContratoPseudoPreenchido = retorno['informacoes_personalizadas']
        self.contratoPseudoPreenchido.addInformacaoPseudo(retornoContratoPseudoPreenchido)
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
                    print(self.finalDict)
                    self.contract.setContractData(self.finalDict)
                    self.formPdf()
                    self.parent.addContratoPseudoPreenchido(self.contratoPseudoPreenchido)
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
                    self.parent.addContratoPseudoPreenchido(self.contratoPseudoPreenchido)
                    self.parent.show_frame("telaAssinaturaDocumento")
                    self.parent.frames["telaAssinaturaDocumento"].show_contentASSINA(id, self.titulo, self.tipo)

        self.pagina +=1

    def prosseguirSemInformacoesPersonalizadas(self):
        if self.tipo == "Consultoria Tributária" or self.tipo == "Câmara de Arbitragem":
            not self.erroTodosOsCampos(self.get_informacoesEmpresariais())
            retorno = self.get_informacoesEmpresariais()
        elif self.tipo == "Consultoria Empresarial":
            match self.pagina:
                case 0:
                    not self.erroTodosOsCampos(self.get_informacoesContratado("Contratante"))
                    self.contratoPseudoPreenchido.addInformacaoPseudo(self.get_informacoesContratado("Contratante"),"Contratante")
                    retorno = None
                case 1:
                    not self.erroTodosOsCampos(self.get_informacoesContratado("Contratada"))
                    self.contratoPseudoPreenchido.addInformacaoPseudo(self.get_informacoesContratado("Contratada"),"Contratada")
                    retorno = None
                case 2:
                    not self.erroTodosOsCampos(self.get_informacoesNegocio())
                    retorno = self.get_informacoesNegocio()
        self.contratoPseudoPreenchido.addInformacaoPseudo(retorno)
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
                    self.clear_check_screen()
                    self.contract.setContractData(self.finalDict)
                    self.formPdf()
                    self.parent.addContratoPseudoPreenchido(self.contratoPseudoPreenchido)
                    self.parent.show_frame("telaAssinaturaDocumento")
                    self.parent.frames["telaAssinaturaDocumento"].show_contentASSINA(id, self.titulo, self.tipo)
            self.pagina +=1
        else:
            self.clear_check_screen()
            self.contract.setContractData(self.finalDict)
            self.formPdf()
            self.parent.addContratoPseudoPreenchido(self.contratoPseudoPreenchido)
            self.parent.show_frame("telaAssinaturaDocumento")
            self.parent.frames["telaAssinaturaDocumento"].show_contentASSINA(id, self.titulo, self.tipo)

    def formPdf(self):
        pdf_saida = './pdfs/pdf_final.pdf'
        if self._checkboxPDF_var.get():
            papel_timbrado = './pdfs/PapelTimbrado_em_Branco_Jus.pdf'
        else:
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
        TitleLable = ctk.CTkLabel(self.frame, text="Informações Empresariais", fg_color="#6EC1E4", font=('Helvetica', 24))
        TitleLable.grid(row=0, column=0, padx=30, pady=40)

        self.frame.grid_columnconfigure(1, minsize=100)
        self.frame.grid_columnconfigure(2, minsize=100)
        self.frame.grid_columnconfigure(3, minsize=100)
        self.frame.grid_columnconfigure(4, minsize=300)

        self.Nome = ctk.CTkLabel(self.frame, text="Nome da Empresa", fg_color="#6EC1E4")
        self.Nome.grid(row=1, column=0, padx=50, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.NomeEntry = ctk.CTkEntry(self.frame, height=30)
        self.NomeEntry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo("nome_empresa"))  # Define o texto inicial
        self.NomeEntry.grid(row=2, column=0, columnspan=4, padx=(40, 20), pady=(0, 30), sticky="ew")

        self.Cnpj = ctk.CTkLabel(self.frame, text="CNPJ", fg_color="#6EC1E4")
        self.Cnpj.grid(row=1, column=4, padx=30, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.CnpjEntry = ctk.CTkEntry(self.frame, height=30)
        self.CnpjEntry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo("cnpj"))  # Define o texto inicial
        self.CnpjEntry.grid(row=2, column=4, columnspan=3, padx=(20, 40), pady=(0, 30), sticky="ew")

        self.Cnae1 = ctk.CTkLabel(self.frame, text="CNAE Principal", fg_color="#6EC1E4")
        self.Cnae1.grid(row=3, column=0, padx=50, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.Cnae1Entry = ctk.CTkEntry(self.frame, height=30)
        self.Cnae1Entry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo("cnae_principal"))  # Define o texto inicial
        self.Cnae1Entry.grid(row=4, column=0, columnspan=2, padx=(40, 20), pady=(0, 30), sticky="ew")

        self.Cnae2 = ctk.CTkLabel(self.frame, text="CNAE Secundário", fg_color="#6EC1E4")
        self.Cnae2.grid(row=3, column=2, padx=30, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.Cnae2Entry = ctk.CTkEntry(self.frame, height=30)
        self.Cnae2Entry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo("cnae_secundaria"))  # Define o texto inicial
        self.Cnae2Entry.grid(row=4, column=2, columnspan=2, padx=20, pady=(0, 30), sticky="ew")

        self.Cfop = ctk.CTkLabel(self.frame, text="CFOP Principais Produtos", fg_color="#6EC1E4")
        self.Cfop.grid(row=3, column=4, padx=30, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.CfopEntry = ctk.CTkEntry(self.frame, height=30)
        self.CfopEntry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo("cfop_principais"))  # Define o texto inicial
        self.CfopEntry.grid(row=4, column=4, columnspan=3, padx=(20, 40), pady=(0, 30), sticky="ew")

        self.IndustriaSetor = ctk.CTkLabel(self.frame, text="Indústria/Setor", fg_color="#6EC1E4")
        self.IndustriaSetor.grid(row=5, column=0, padx=50, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.IndustriaSetorEntry = ctk.CTkEntry(self.frame, height=30)
        self.IndustriaSetorEntry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo("industria_setor"))  # Define o texto inicial
        self.IndustriaSetorEntry.grid(row=6, column=0, columnspan=2, padx=(40, 20), pady=(0, 30), sticky="ew")

        self.ReceitaAnual = ctk.CTkLabel(self.frame, text="Receita Anual", fg_color="#6EC1E4")
        self.ReceitaAnual.grid(row=5, column=2, padx=30, pady=5, sticky="w")

        # Combobox para Receita Anual
        opcoesR = ["Até R$81 mil", "R$81 mil a R$360 mil", "R$360 mil a R$4,8 milhões", "R$4,8 milhões a R$78 milhões", "Superior a R$78 milhões"]
        self.selectboxR = ttk.Combobox(self.frame, values=opcoesR)
        self.selectboxR.grid(row=6, column=2, columnspan=2, padx=20, pady=(0, 30), sticky="ew")
        self.selectboxR.set("Selecione a Receita Anual")

        if not self.camposPersonalizados:
            self._checkboxPDF_var = ctk.BooleanVar()
            self._checkboxPDF = ctk.CTkCheckBox(self, text="Template Branco", variable=self._checkboxPDF_var)
            self._checkboxPDF.pack(side=ctk.TOP, pady=(30, 0), padx=(500, 0), anchor="w")
            self.button_frame.destroy()
            # Frame para agrupar os botões
            self.button_frame = ctk.CTkFrame(self)
            self.button_frame.pack(pady=(30, 0), padx=(500, 0))

            # Botão Voltar
            self.voltar = ctk.CTkButton(self.button_frame, text="Voltar", command=partial(self.voltar_funcao, False), height=30)
            self.voltar.pack(padx=10,side=ctk.LEFT)

            # Botão Prosseguir
            self.buttonContinue = ctk.CTkButton(self.button_frame, text="Prosseguir", command=self.prosseguir_funcao, height=30, width=300)
            self.buttonContinue.pack(side=ctk.LEFT, padx=(0, 10))




    def informacoesContratante(self, parte: str):
        # Label dentro do frame filho
        if parte == "Contratante":
            text = "Informações do Contratante"
        elif parte == "Contratada":
            text = "Informações da Contratada"

        TitleLable = ctk.CTkLabel(self.frame, text=text, fg_color="#6EC1E4", font=('Helvetica', 24))
        TitleLable.grid(row=0, column=0, padx=30, pady=40)

        self.frame.grid_columnconfigure(1, minsize=100)
        self.frame.grid_columnconfigure(2, minsize=100)
        self.frame.grid_columnconfigure(3, minsize=100)
        self.frame.grid_columnconfigure(4, minsize=300)

        self.Nome = ctk.CTkLabel(self.frame, text="Nome Completo", fg_color="#6EC1E4")
        self.Nome.grid(row=1, column=0, padx=50, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.NomeContractEntry = ctk.CTkEntry(self.frame, height=30)
        self.NomeContractEntry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo(parte + "nome"))  # Define o texto inicial
        self.NomeContractEntry.grid(row=2, column=0, columnspan=4, padx=(40, 20), pady=(0, 30), sticky="ew")

        self.Nacionalidade = ctk.CTkLabel(self.frame, text="Nacionalidade", fg_color="#6EC1E4")
        self.Nacionalidade.grid(row=1, column=4, padx=30, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.NacionalidadeEntry = ctk.CTkEntry(self.frame, height=30)
        self.NacionalidadeEntry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo(parte + "nacionalidade"))  # Define o texto inicial
        self.NacionalidadeEntry.grid(row=2, column=4, columnspan=3, padx=(20, 40), pady=(0, 30), sticky="ew")

        self.EstadoCivil = ctk.CTkLabel(self.frame, text="Estado Civil", fg_color="#6EC1E4")
        self.EstadoCivil.grid(row=3, column=0, padx=50, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.EstadoCivilEntry = ctk.CTkEntry(self.frame, height=30)
        self.EstadoCivilEntry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo(parte + "estadocivil"))  # Define o texto inicial
        self.EstadoCivilEntry.grid(row=4, column=0, columnspan=2, padx=(40, 20), pady=(0, 30), sticky="ew")

        self.Profissao = ctk.CTkLabel(self.frame, text="Profissão", fg_color="#6EC1E4")
        self.Profissao.grid(row=3, column=2, padx=30, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.ProfissaoEntry = ctk.CTkEntry(self.frame, height=30)
        self.ProfissaoEntry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo(parte + "profissao"))  # Define o texto inicial
        self.ProfissaoEntry.grid(row=4, column=2, columnspan=2, padx=20, pady=(0, 30), sticky="ew")

        self.CpfOuCnpj = ctk.CTkLabel(self.frame, text="CPF ou CNPJ", fg_color="#6EC1E4")
        self.CpfOuCnpj.grid(row=3, column=4, padx=30, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.CpfOuCnpjEntry = ctk.CTkEntry(self.frame, height=30)
        self.CpfOuCnpjEntry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo(parte + "cpf"))  # Define o texto inicial
        self.CpfOuCnpjEntry.grid(row=4, column=4, columnspan=3, padx=(20, 40), pady=(0, 30), sticky="ew")

        self.Endereco = ctk.CTkLabel(self.frame, text="Endereço de Residência ou Comercial", fg_color="#6EC1E4")
        self.Endereco.grid(row=5, column=0, padx=50, pady=5, sticky="w")

        # Entry dentro do frame filho
        self.EnderecoEntry = ctk.CTkEntry(self.frame, height=30)
        self.EnderecoEntry.insert(0, self.contratoPseudoPreenchido.getInformacaoPseudo(parte + "endereco"))  # Define o texto inicial
        self.EnderecoEntry.grid(row=6, column=0, columnspan=2, padx=(40, 20), pady=(0, 30), sticky="ew")

        self.Qualificacao = ctk.CTkLabel(self.frame, text="Qualificação da Parte", fg_color="#6EC1E4")
        self.Qualificacao.grid(row=5, column=2, padx=30, pady=5, sticky="w")


        qualiContratante = ["Contratante de Serviços", "Arrendador", "Outorgante", "Cedente", "Vendedor", "Locador",
                            "Franqueador", "Empregador"]
        qualiContratado = ["Prestador de Serviços", "Arrendatário", "Outorgado", "Cessionário", "Comprador", "Locatário",
                        "Franqueado", "Empregado"]

        if parte == "Contratante":
            self.selectbox = ttk.Combobox(self.frame, values=qualiContratante)
            self.selectbox.grid(row=6, column=2, columnspan=2, padx=20, pady=(0, 30), sticky="ew")
            self.selectbox.set("Qualificação")
        elif parte == "Contratada":
            self.selectbox = ttk.Combobox(self.frame, values=qualiContratado)
            self.selectbox.grid(row=6, column=2, columnspan=2, padx=20, pady=(0, 30), sticky="ew")
            self.selectbox.set("Qualificação")



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
        self.ValorEntry.insert(0,self.contratoPseudoPreenchido.getInformacaoPseudo("valor"))
        self.ValorEntry.grid(row=2, column=0, columnspan=4, padx=(40,20), pady=(0,30),sticky="ew")

        self.FormaPagamento = ctk.CTkLabel(self.frame, text="Forma de Pagamento",fg_color="#6EC1E4")
        self.FormaPagamento.grid(row=1, column=4, padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.FormaPagamentoEntry = ctk.CTkEntry(self.frame,height=30)
        self.FormaPagamentoEntry.insert(0,self.contratoPseudoPreenchido.getInformacaoPseudo("forma_pagamento"))
        self.FormaPagamentoEntry.grid(row=2, column=4, columnspan=3, padx=(20,40), pady=(0,30),sticky="ew")

        self.MultaDeMora = ctk.CTkLabel(self.frame, text="Multa de Mora",fg_color="#6EC1E4")
        self.MultaDeMora.grid(row=3, column=0,padx=50, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.MultaDeMoraEntry = ctk.CTkEntry(self.frame,height=30)
        self.MultaDeMoraEntry.insert(0,self.contratoPseudoPreenchido.getInformacaoPseudo("multa_mora"))
        self.MultaDeMoraEntry.grid(row=4, column=0, columnspan=2, padx=(40,20), pady=(0,30),sticky="ew")

        self.JurosDeMora = ctk.CTkLabel(self.frame, text="Juros de Mora",fg_color="#6EC1E4")
        self.JurosDeMora.grid(row=3, column=2, padx=30, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.JurosDeMoraEntry = ctk.CTkEntry(self.frame,height=30)
        self.JurosDeMoraEntry.insert(0,self.contratoPseudoPreenchido.getInformacaoPseudo("juros_mora"))
        self.JurosDeMoraEntry.grid(row=4, column=2, columnspan=2, padx=20, pady=(0,30),sticky="ew")

        self.CorrecaoMonetaria = ctk.CTkLabel(self.frame, text="Correção Monetária",fg_color="#6EC1E4")
        self.CorrecaoMonetaria.grid(row=3, column=4, padx=30, pady=5,sticky="w")

        self.PrazoDuracao = ctk.CTkLabel(self.frame, text="Prazo de Duração",fg_color="#6EC1E4")
        self.PrazoDuracao.grid(row=5,column = 0, padx=50, pady=5,sticky="w")

        # Entry dentro do frame filho
        self.PrazoDuracaoEntry = ctk.CTkEntry(self.frame,height=30)
        self.PrazoDuracaoEntry.insert(0,self.contratoPseudoPreenchido.getInformacaoPseudo("prazo_duracao"))
        self.PrazoDuracaoEntry.grid(row=6, column=0, columnspan=2, padx=(40,20), pady=(0,30),sticky="ew")

        # Correção Monetária

        opcoesCM = ["IGP-M", "INPC", "IPCA", "POUPANÇA", "SELIC", "CDI"]
        self.selectboxCM = ttk.Combobox(self.frame, values=opcoesCM)
        self.selectboxCM.grid(row=4, column=4, columnspan=3, padx=(20, 40), pady=(0, 30), sticky="ew")
        #self.contratoPseudoPreenchido.getInformacaoPseudo("correcao_monetaria")
        self.selectboxCM.set("Correção Monetária")

        if not self.camposPersonalizados:
            self._checkboxPDF_var = ctk.BooleanVar()
            self._checkboxPDF = ctk.CTkCheckBox(self, text="Template Branco", variable=self._checkboxPDF_var)
            self._checkboxPDF.pack(side=ctk.TOP, pady=(30, 0), padx=(500, 0), anchor="w")
            self.button_frame.destroy()
            # Frame para agrupar os botões
            self.button_frame = ctk.CTkFrame(self)
            self.button_frame.pack(pady=(30, 0), padx=(500, 0))

            # Botão Voltar
            self.voltar = ctk.CTkButton(self.button_frame, text="Voltar", command=partial(self.voltar_funcao, False), height=30)
            self.voltar.pack(padx=10,side=ctk.LEFT)

            # Botão Prosseguir
            self.buttonContinue = ctk.CTkButton(self.button_frame, text="Prosseguir", command=self.prosseguir_funcao, height=30, width=300)
            self.buttonContinue.pack(side=ctk.LEFT, padx=(0, 10))

    def informacoesPersonalizadas(self):
        self.frame.destroy()
        self.buttonContinue.destroy()
        self.voltar.destroy()
        self.button_frame.destroy()
        self.frame = ctk.CTkScrollableFrame(self.frameScroll,height=400,width=900,**self.framePrincipal)
        self.frame.pack(pady=(80, 0))

        self._checkboxPDF_var = ctk.BooleanVar()
        self._checkboxPDF = ctk.CTkCheckBox(self.frameScroll, text="Template Branco", variable=self._checkboxPDF_var)
        self._checkboxPDF.pack(side=ctk.TOP, pady=(30, 0), padx=(500, 0), anchor="w")

        # Frame para agrupar os botões
        self.button_frame = ctk.CTkFrame(self.frameScroll)
        self.button_frame.pack(pady=(30, 0), padx=(500, 0))

        # Botão Voltar
        self.voltar = ctk.CTkButton(self.button_frame, text="Voltar", command=partial(self.voltar_funcao, False), height=30)
        self.voltar.pack(padx=10,side=ctk.LEFT)

        # Botão Prosseguir
        self.buttonContinue = ctk.CTkButton(self.button_frame, text="Prosseguir", command=self.prosseguir_funcao, height=30, width=300)
        self.buttonContinue.pack(side=ctk.LEFT, padx=(0, 10))

        self.tituloInformacoesPersonalizadas = ctk.CTkLabel(self.frame, text="Informações Adicionais",fg_color="#6EC1E4",font =('Helvetica', 24))
        self.tituloInformacoesPersonalizadas.pack(padx=30, pady=(20,40),anchor="w")

        self.camposPersonalizadosEntry = []
        for i,campo in enumerate(self.camposPersonalizados):
            self.camposPersonalizadosLable = ctk.CTkLabel(self.frame, text=campo,fg_color="#6EC1E4")
            self.camposPersonalizadosLable.pack(padx=(280,0),pady=5,anchor="w")

            self.camposPersonalizadosEntry.append(ctk.CTkEntry(self.frame,height=30,width=400))
            self.camposPersonalizadosEntry[i].insert(0,self.contratoPseudoPreenchido.getInformacaoPseudo(campo))
            self.camposPersonalizadosEntry[i].pack(padx=(40,20), pady=(0,30))

    def contratoNaoEncontrado(self):
        frameErro = {
            "corner_radius": 30,
            "border_width": 2,
            "fg_color": ["#D27C7C", "#D27C7C"],
            "border_color": ["#C23E3E", "#C23E3E"]
        }
        self.frame.configure(**frameErro)
        self.errorText = ctk.CTkLabel(self.frame, text="Contrato Não Encontrado no Banco de Dados, a equipe JUS está trabalhando nisso", font=("Consolas", 17, 'bold'), text_color="#EFEFEF")
        self.frame.pack_propagate(False)
        self.errorText.pack(expand = True, fill= ctk.BOTH,padx = 20,pady = 20)
        self.buttonContinue.pack_forget()

    def get_informacoesNegocio(self):
        contract_data = {
		'valor': self.ValorEntry.get(),
		'forma_pagamento': self.FormaPagamentoEntry.get(),
		'multa_mora': self.MultaDeMoraEntry.get(),
		'juros_mora': self.JurosDeMoraEntry.get(),
		'correcao_monetaria': self.selectboxCM.get(),
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
            'receita_anual': self.selectboxR.get()
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
                'endereco': self.EnderecoEntry.get(),
                'qualificaco_da_parte' : self.selectbox.get()
            }
            return self.contratante_data
        elif contratante == "Contratada":
            self.contratado_data = {
                'nome': self.NomeContractEntry.get(),
                'nacionalidade': self.NacionalidadeEntry.get(),
                'estadocivil': self.EstadoCivilEntry.get(),
                'cpf': self.CpfOuCnpjEntry.get(),
                'profissao': self.ProfissaoEntry.get(),
                'endereco': self.EnderecoEntry.get(),
                'qualificaco_da_parte' : self.selectbox.get()
            }
            return self.contratado_data

    def get_informacoesPersonalizadas(self):
        # Cria um dicionário para armazenar as informações personalizadas
        dictInformacoes = {}

        # Percorre a lista de entradas e coleta os valores
        for i, entrada in enumerate(self.camposPersonalizadosEntry):
            dictInformacoes[self.camposPersonalizados[i]] = entrada.get()

        # Retorna o dicionário dentro de outro dicionário
        return {'informacoes_personalizadas':dictInformacoes}


    def voltar_funcao(self,contratoNaoEncontrado):
        if not contratoNaoEncontrado:
            self.parent.addContratoPseudoPreenchido(self.contratoPseudoPreenchido)
        self.unbind("<Configure>")
        for widget in self.winfo_children():
            widget.destroy()
        self.parent.show_frame("telaPrincipal")
        self.parent.frames["telaPrincipal"].show_content()

    def load_and_resize_imageQuali(self, image_path, size):
        image = Image.open(self.relative_to_assetsQuali(image_path))
        resized_image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def relative_to_assetsQuali(self, path: str) -> Path:
        ASSETS_PATH = Path(os.path.dirname(os.path.abspath(__file__))) / 'Cadastro_Usuario' / 'assets'/ 'frame0'
        return ASSETS_PATH / Path(path)

    # def show_qualificacaoContratante_menu(self):
    #     self.qualificacaoContratante_menu.post(self.qualificacaoContratante_button.winfo_rootx(), self.qualificacaoContratante_button.winfo_rooty() + self.qualificacaoContratante_button.winfo_height())

    def select_qualificacaoContratante(self, quali):
        self.selected_quali = quali
        self.qualificacaoContratante_button.config(text=quali)

    def load_and_resize_imageCM(self, image_path, size):
        image = Image.open(self.relative_to_assetsCM(image_path))
        resized_image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def relative_to_assetsCM(self, path: str) -> Path:
        ASSETS_PATH = Path(os.path.dirname(os.path.abspath(__file__))) / 'Cadastro_Usuario' / 'assets'/ 'frame0'
        return ASSETS_PATH / Path(path)

    def show_correcao_menu(self):
        self.correcao_menu.post(self.correcao_button.winfo_rootx(), self.correcao_button.winfo_rooty() + self.correcao_button.winfo_height())

    def select_correcao(self, correcao):
        self.selected_correcao = correcao
        self.correcao_button.config(text=correcao)

    def show_receita_menu(self):
        self.receita_menu.post(self.receita_button.winfo_rootx(), self.receita_button.winfo_rooty() + self.receita_button.winfo_height())

    def select_receita(self, receita):
        self.selected_receita = receita
        self.receita_button.config(text=receita)


    def erroTodosOsCampos(self,dicionario):
        for chave, valor in dicionario.items():
            if valor is None or valor == "":
                messagebox.showerror(
            "Erro", "Todos os campos devem ser preenchidos!")
                return False
        return True
