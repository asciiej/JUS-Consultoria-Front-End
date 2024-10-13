import tkinter
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from ..utilitarios.user_session import USER_SESSION
from functools import partial
from src.interface.checagemInformacoes import checagemInformacoes
from .Atualizar_dados.atualizarinform import AtualizaCad
#from src.classes.usuario.usuarioModel import usuarioModel

class telaPrincipal(ctk.CTkFrame):
    def __init__(self,parent,controlers : dict):
        super().__init__(parent)
        self.parent = parent
        self.controlers = controlers
        ctk.set_default_color_theme("lib/temaTkinterCustom.json")

        self.framePrincipal = {
            "corner_radius": 30,
            "border_width": 2,
            "fg_color": ["#6EC1E4", "#6EC1E4"],
            "border_color": ["#00343D", "#00343D"]
        }

    def click_consultoria_empresarial(self):
        self.canvas.yview_moveto((self.H1_consultoria_empresarial.winfo_y() - 150  ) / self.body_frame.winfo_height())

    def click_consultoria_tributaria(self):
        self.canvas.yview_moveto((self.H1_consultoria_tributaria.winfo_y() - 100) / self.body_frame.winfo_height())

    def click_camara_arbitragem(self):
        self.canvas.yview_moveto((self.H1_camara_arbitragem.winfo_y() - 100) / self.body_frame.winfo_height())

    def click_editar_dados(self):
        self.unbind("<Configure>")
        for widget in self.winfo_children():
            widget.destroy()
        self.parent.show_frame("AtualizaCad")
        self.parent.frames["AtualizaCad"].show_contentATUALIZAR()



    def on_frame_configure(self, event):

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.canvas.xview_moveto(0.179)

    def on_window_resize(self, event):

        self.canvas.xview_moveto(0.179)

    def activate_scroll(self, event):
        self.body_frame.bind("<MouseWheel>", self.on_mousewheel)

    def deactivate_scroll(self, event):
        self.body_frame.unbind("<MouseWheel>")

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def choose_contract(self, titulo, tipo):
        self.unbind("<Configure>")
        for widget in self.winfo_children():
            widget.destroy()
        self.parent.show_frame("checagemInformacoes")
        self.parent.frames["checagemInformacoes"].show_contentCHECA(id, tipo, titulo, self.controlers)

    def show_content(self):

        
        #self.janela = janela
        self.font = ctk.CTkFont('Helvetica',14)

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
        self.logoJUS = ctk.CTkImage(Image.open('imagens/Logomarca JUS.png'),size = (80,72.54))
        self.logo_cabecalho = ctk.CTkLabel(self.cabecalho, image=self.logoJUS, text = "")
        self.logo_cabecalho.pack(side=ctk.LEFT, padx=(18, 0), pady=7)

        # Usuario foto
        self.userPic = ctk.CTkImage(Image.open('imagens/User Male Black.png'), size = (90,90))
        self.userPic_cabecalho = ctk.CTkLabel(self.cabecalho, image=self.userPic, text = "")
        self.userPic_cabecalho.pack(side=ctk.RIGHT, padx=(0, 18), pady=7)


        # Botão menu personalizado
        opcao_menu = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#6EC1E4", "#6EC1E4"],
            "hover_color": ["#6EC1E4", "#6EC1E4"],
            "border_color": ["#6EC1E4", "#6EC1E4"],
            "text_color": "#000000",
            "text_color_disabled": ["#6EC1E4", "#6EC1E4"]
        }
        
        # Botões menu
        if USER_SESSION.has_role('empresarial'):
            self.botao_consultoria_empresarial = ctk.CTkButton(self.cabecalho, text="Consultoria Empresarial", command=self.click_consultoria_empresarial, **opcao_menu)
            self.botao_consultoria_empresarial.pack(side=ctk.LEFT, padx=(25,0))

        if USER_SESSION.has_role('tributaria'):
            self.botao_consultoria_tributaria = ctk.CTkButton(self.cabecalho, text="Consultoria Tributária", command=self.click_consultoria_tributaria, **opcao_menu)
            self.botao_consultoria_tributaria.pack(side=ctk.LEFT, padx=(25,0))

        if USER_SESSION.has_role('arbitragem'):
            self.botao_camara_arbitragem = ctk.CTkButton(self.cabecalho, text="Câmara de Arbitragem", command=self.click_camara_arbitragem, **opcao_menu)
            self.botao_camara_arbitragem.pack(side=ctk.LEFT, padx=(25,0))

        # Nome do usuario no cabeçalho
        self.nome_usuario_label = ctk.CTkLabel(self.cabecalho, text=f"{USER_SESSION.get_user_data().nome} {USER_SESSION.get_user_data().sobrenome}", font=self.font)
        self.nome_usuario_label.pack(side=ctk.RIGHT, padx=(0, 25))

        self.botao_editar_dados = ctk.CTkButton(self.cabecalho, text="Editar", command=self.click_editar_dados, **opcao_menu)
        self.botao_editar_dados.pack(side=ctk.LEFT, padx=(25,0))

        # Calcular a altura do "body"
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        header_height = self.cabecalho.winfo_height()
        body_height = window_height - header_height

        body = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#EFEFEF", "#EFEFEF"]

        }

        #Barra Scroll
        self.canvas = ctk.CTkCanvas(self, height=body_height)
        self.canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

        #Body da pagina
        self.body_frame = ctk.CTkFrame(self.canvas, **body)
        self.body_frame.pack(fill=ctk.BOTH)

        #Adicionando scrollbar vertical
        self.vertical_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.vertical_scrollbar.pack(side="right", fill="y")

        #Controle do scroll
        self.canvas.configure(yscrollcommand=self.vertical_scrollbar.set)

        #Rodinha da barra
        self.canvas.create_window((0, 0), window=self.body_frame, anchor="nw")


        #Configurar o evento de rolagem para o Canvas
        self.body_frame.bind("<Configure>", self.on_frame_configure)

        # Configurar o evento de rolagem para o mouse
        self.body_frame.bind("<Enter>", self.activate_scroll)
        self.body_frame.bind("<Leave>", self.deactivate_scroll)


        # Card customizado
        card = {
            "corner_radius": 20,  # Adiciona um raio de canto de 10
            "width": 230,   # Largura
            "height": 230,  # Altura
            "fg_color": "#EFEFEF",  # Cor de fundo do quadrado
            "border_width": 2,
            "border_color": "#00343D",  # Cor da borda
        }

        botao = {
            "corner_radius": 20,
            "border_width": 0,
            "width": 160,
            "height": 36,
            "fg_color": ["#325564", "#325564"],
            "hover_color": ["#183E4F", "#183E4F"],
            "border_color": ["#6EC1E4", "#6EC1E4"],
            "text_color": "#EFEFEF",
            "text_color_disabled": ["#EFEFEF", "#EFEFEF"]
        }

        if USER_SESSION.has_role('empresarial'):
        #Consultoria Empresarial
        #Título
            self.H1_consultoria_empresarial = ctk.CTkLabel(self.body_frame, text="Consultoria Empresarial", font=("Consolas", 40))
            self.H1_consultoria_empresarial.pack(side=ctk.TOP, pady=(80 ,20))

            #Frame
            self.frame_consultoria_empresarial = ctk.CTkScrollableFrame(self.body_frame, height=280, width=900,**self.framePrincipal)
            self.frame_consultoria_empresarial.pack()

        #Primeira linha
            self.square1_1 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square1_1.grid(row = 0,column=0,padx = 20,pady = 20)
            self.square1_1.pack_propagate(False)
            #Imagem
            self.img1_1 = ctk.CTkImage(Image.open('imagens/Profissional.png'), size=(200, 72))
            self.img_label1_1 = ctk.CTkLabel(self.square1_1, image=self.img1_1, text="")
            self.img_label1_1.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_1_1 = ctk.CTkLabel(self.square1_1, text="CONTRATO DE PRESTAÇÃO DE\nSERVIÇOS PROFISSIONAIS", font=("Calibri", 15))
            self.h2_1_1.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button1_1 = ctk.CTkButton(self.square1_1, text="Contrate", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Prestação de Serviços Profissionais"), **botao)
            self.button1_1.pack(side=ctk.BOTTOM, pady=(0, 45))

            self.square1_2 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square1_2.grid(row = 0,column=1,padx = 50,pady = 20)
            self.square1_2.pack_propagate(False)
            #Imagem
            self.img1_2 = ctk.CTkImage(Image.open('imagens/Hospitalar.png'), size=(200, 72))
            self.img_label1_2 = ctk.CTkLabel(self.square1_2, image=self.img1_2, text="")
            self.img_label1_2.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_1_2 = ctk.CTkLabel(self.square1_2, text="CONTRATO DE PRESTAÇÃO DE\nSERVIÇOS MÉDICO-HOSPITALAR", font=("Calibri", 15))
            self.h2_1_2.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button1_2 = ctk.CTkButton(self.square1_2, text="Contrate", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Prestação de Serviços Médico-Hospitalar"), **botao)
            self.button1_2.pack(side=ctk.BOTTOM, pady=(0, 45))

            self.square1_3 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square1_3.grid(row = 0,column=2,padx = 20,pady = 20)
            self.square1_3.pack_propagate(False)
            #Imagem
            self.img1_3 = ctk.CTkImage(Image.open('imagens/Mercantil.png'), size=(200, 72))
            self.img_label1_3 = ctk.CTkLabel(self.square1_3, image=self.img1_3, text="")
            self.img_label1_3.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_1_3 = ctk.CTkLabel(self.square1_3, text="CONTRATO DE COMPRA E\nVENDA MERCANTIL", font=("Calibri", 15))
            self.h2_1_3.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button1_3 = ctk.CTkButton(self.square1_3, text="Contrate", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Compra e Venda Mercantil"), **botao)
            self.button1_3.pack(side=ctk.BOTTOM, pady=(0, 45))


            #Segunda linha

            self.square2_1 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square2_1.grid(row = 1,column=0,padx= 20,pady = 20)
            self.square2_1.pack_propagate(False)
            #Imagem
            self.img2_1 = ctk.CTkImage(Image.open('imagens/Imovel.png'), size=(200, 72))
            self.img_label2_1 = ctk.CTkLabel(self.square2_1, image=self.img2_1, text="")
            self.img_label2_1.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_2_1 = ctk.CTkLabel(self.square2_1, text="CONTRATO DE COMPRA E\nVENDA DE IMÓVEL", font=("Calibri", 15))
            self.h2_2_1.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button2_1 = ctk.CTkButton(self.square2_1, text="Contrate", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Compra e Venda de Imóvel"), **botao)
            self.button2_1.pack(side=ctk.BOTTOM, pady=(0, 45))

            self.square2_2 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square2_2.grid(row = 1,column=1,padx = 20,pady = 20)
            self.square2_2.pack_propagate(False)
            #Imagem
            self.img2_2 = ctk.CTkImage(Image.open('imagens/LocacaoImovel.png'), size=(200, 72))
            self.img_label2_2 = ctk.CTkLabel(self.square2_2, image=self.img2_2, text="")
            self.img_label2_2.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_2_2 = ctk.CTkLabel(self.square2_2, text="CONTRATO DE LOCAÇÃO DE\nIMÓVEL", font=("Calibri", 15))
            self.h2_2_2.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button2_2 = ctk.CTkButton(self.square2_2, text="Contrate",command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Locação de Imóvel"), **botao)
            self.button2_2.pack(side=ctk.BOTTOM, pady=(0, 45))

            self.square2_3 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square2_3.grid(row = 1,column=2,padx = 20,pady = 20)
            self.square2_3.pack_propagate(False)
            #Imagem
            self.img2_3 = ctk.CTkImage(Image.open('imagens/Rural.png'), size=(200, 72))
            self.img_label2_3 = ctk.CTkLabel(self.square2_3, image=self.img2_3, text="")
            self.img_label2_3.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_2_3 = ctk.CTkLabel(self.square2_3, text="CONTRATO DE ARRENDAMENTO\nRURAL", font=("Calibri", 15))
            self.h2_2_3.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button2_3 = ctk.CTkButton(self.square2_3, text="Contrate",command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Arrendamento Rural"), **botao)
            self.button2_3.pack(side=ctk.BOTTOM, pady=(0, 45))

            #Terceira linha

            self.square3_1 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square3_1.grid(row = 2,column=0,padx= 20,pady = 20)
            self.square3_1.pack_propagate(False)
            #Imagem
            self.img3_1 = ctk.CTkImage(Image.open('imagens/Agricola.png'), size=(200, 72))
            self.img_label3_1 = ctk.CTkLabel(self.square3_1, image=self.img3_1, text="")
            self.img_label3_1.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_3_1 = ctk.CTkLabel(self.square3_1, text="CONTRATO DE PARCERIA\nAGRÍCOLA", font=("Calibri", 15))
            self.h2_3_1.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button3_1 = ctk.CTkButton(self.square3_1, text="Contrate", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Parceria Agrícola"), **botao)
            self.button3_1.pack(side=ctk.BOTTOM, pady=(0, 45))

            self.square3_2 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square3_2.grid(row = 2,column=1,padx = 20,pady = 20)
            self.square3_2.pack_propagate(False)
            #Imagem
            self.img3_2 = ctk.CTkImage(Image.open('imagens/Software.png'), size=(200, 72))
            self.img_label3_2 = ctk.CTkLabel(self.square3_2, image=self.img3_2, text="")
            self.img_label3_2.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_3_2 = ctk.CTkLabel(self.square3_2, text="CONTRATO DE LICENÇA DE USO\nDE SOFTWARE", font=("Calibri", 15))
            self.h2_3_2.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button3_2 = ctk.CTkButton(self.square3_2, text="Contrate", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Licença de Uso de Software"), **botao)
            self.button3_2.pack(side=ctk.BOTTOM, pady=(0, 45))


        #Quarta linha

            self.square4_1 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square4_1.grid(row = 2,column=2,padx= 20,pady = 20)
            self.square4_1.pack_propagate(False)
            #Imagem
            self.img4_1 = ctk.CTkImage(Image.open('imagens/Intelectual.png'), size=(200, 72))
            self.img_label4_1 = ctk.CTkLabel(self.square4_1, image=self.img4_1, text="")
            self.img_label4_1.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_4_1 = ctk.CTkLabel(self.square4_1, text="CONTRATO DE LICENÇA E CESSÃO\nDE DIREITOS DE USO DE\nPROPRIEDADE INTELECTUAL", font=("Calibri", 15))
            self.h2_4_1.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button4_1 = ctk.CTkButton(self.square4_1, text="Contrate", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Licença de Cessão de Direitos de Uso de Propriedade Intelectual"), **botao)
            self.button4_1.pack(side=ctk.BOTTOM, pady=(0, 36))

            self.square4_2 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square4_2.grid(row = 3,column=0,padx = 20,pady = 20)
            self.square4_2.pack_propagate(False)
            #Imagem
            self.img4_2 = ctk.CTkImage(Image.open('imagens/Franquia.png'), size=(200, 72))
            self.img_label4_2 = ctk.CTkLabel(self.square4_2, image=self.img4_2, text="")
            self.img_label4_2.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_4_2 = ctk.CTkLabel(self.square4_2, text="CONTRATO DE FRANQUIA", font=("Calibri", 15))
            self.h2_4_2.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button4_2 = ctk.CTkButton(self.square4_2, text="Contrate", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Franquia"), **botao)
            self.button4_2.pack(side=ctk.BOTTOM, pady=(0, 45))

            self.square4_3 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square4_3.grid(row = 3,column=1,padx = 20,pady = 20)
            self.square4_3.pack_propagate(False)
            #Imagem
            self.img4_3 = ctk.CTkImage(Image.open('imagens/Indeterminado.png'), size=(200, 72))
            self.img_label4_3 = ctk.CTkLabel(self.square4_3, image=self.img4_3, text="")
            self.img_label4_3.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_4_3 = ctk.CTkLabel(self.square4_3, text="CONTRATO DE TRABALHO POR\nPRAZO INDETERMINADO", font=("Calibri", 15))
            self.h2_4_3.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button4_3 = ctk.CTkButton(self.square4_3, text="Contrate", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Trabalho por Prazo Indeterminado"), **botao)
            self.button4_3.pack(side=ctk.BOTTOM, pady=(0, 45))

            self.square5_1 = ctk.CTkFrame(self.frame_consultoria_empresarial, **card)
            self.square5_1.grid(row = 3,column=2,padx = 20,pady = 20)
            self.square5_1.pack_propagate(False)
            #Imagem
            self.img5_1 = ctk.CTkImage(Image.open('imagens/Editar.png'), size=(200, 72))
            self.img_label5_1 = ctk.CTkLabel(self.square5_1, image=self.img5_1, text="")
            self.img_label5_1.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_5_1 = ctk.CTkLabel(self.square5_1, text="Contrato Editável", font=("Calibri", 15))
            self.h2_5_1.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button5_1 = ctk.CTkButton(self.square5_1, text="Contratar", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato Editável Empresarial"), **botao)
            self.button5_1.pack(side=ctk.BOTTOM, pady=(0, 45))


        if USER_SESSION.has_role('tributaria'):
            #Consultoria Tributária

            #Título
            self.H1_consultoria_tributaria = ctk.CTkLabel(self.body_frame, text="Consultoria Tributária", font=("Consolas", 40))
            self.H1_consultoria_tributaria.pack(side=ctk.TOP, pady=(90 ,0))
            #Frame
            self.frame_consultoria_tributaria = ctk.CTkFrame(self.body_frame, height=280, width=950,**self.framePrincipal)
            self.frame_consultoria_tributaria.pack(pady=(40, 0))


            #Primeira linha

            self.square1_1 = ctk.CTkFrame(self.frame_consultoria_tributaria, **card)
            self.square1_1.grid(row = 0,column=0,padx = 20,pady = 20)
            self.square1_1.pack_propagate(False)
            #Imagem
            self.img1_1 = ctk.CTkImage(Image.open('imagens/Tributario.png'), size=(200, 72))
            self.img_label1_1 = ctk.CTkLabel(self.square1_1, image=self.img1_1, text="")
            self.img_label1_1.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_1_1 = ctk.CTkLabel(self.square1_1, text="PARECER TRIBUTÁRIO", font=("Calibri", 15))
            self.h2_1_1.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button1_1 = ctk.CTkButton(self.square1_1, text="Contrate", command=partial(self.choose_contract,"Consultoria Tributária","Parecer Tributário"), **botao)
            self.button1_1.pack(side=ctk.BOTTOM, pady=(0, 45))

            self.square1_2 = ctk.CTkFrame(self.frame_consultoria_tributaria, **card)
            self.square1_2.grid(row = 0,column=1,padx = 50,pady = 20)
            self.square1_2.pack_propagate(False)
            #Imagem
            self.img1_2 = ctk.CTkImage(Image.open('imagens/Planejamento.png'), size=(200, 72))
            self.img_label1_2 = ctk.CTkLabel(self.square1_2, image=self.img1_2, text="")
            self.img_label1_2.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_1_2 = ctk.CTkLabel(self.square1_2, text="PLANEJAMENTO TRIBUTÁRIO", font=("Calibri", 15))
            self.h2_1_2.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button1_2 = ctk.CTkButton(self.square1_2, text="Contrate", command=partial(self.choose_contract,"Consultoria Tributária","Planejamento Tributário"), **botao)
            self.button1_2.pack(side=ctk.BOTTOM, pady=(0, 45))

            self.square1_3 = ctk.CTkFrame(self.frame_consultoria_tributaria, **card)
            self.square1_3.grid(row = 0,column=2,padx = 20,pady = 20)
            self.square1_3.pack_propagate(False)
            #Imagem
            self.img1_3 = ctk.CTkImage(Image.open('imagens/Editar.png'), size=(200, 72))
            self.img_label1_3 = ctk.CTkLabel(self.square1_3, image=self.img1_3, text="")
            self.img_label1_3.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_1_3 = ctk.CTkLabel(self.square1_3, text="Minutas Tributária", font=("Calibri", 15))
            self.h2_1_3.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button1_3 = ctk.CTkButton(self.square1_3, text="Contratar", command=partial(self.choose_contract,"Consultoria Tributária","Contrato Editável Tributária"), **botao)
            self.button1_3.pack(side=ctk.BOTTOM, pady=(0, 45))

        if USER_SESSION.has_role('arbitragem'):

            #Câmara de Arbitragem

            #Título
            self.H1_camara_arbitragem = ctk.CTkLabel(self.body_frame, text="Câmara de Arbitragem", font=("Consolas", 40))
            self.H1_camara_arbitragem.pack(side=ctk.TOP, pady=(90 ,0))
            #Frame
            self.frame_camara_arbitragem = ctk.CTkFrame(self.body_frame, height=280, width=950,**self.framePrincipal)
            self.frame_camara_arbitragem.pack(pady=(40, 0))

            #Primeira linha

            self.square1_1 = ctk.CTkFrame(self.frame_camara_arbitragem, **card)
            self.square1_1.grid(row = 0,column=0,padx = 20,pady = 20)
            self.square1_1.pack_propagate(False)
            #Imagem
            self.img1_1 = ctk.CTkImage(Image.open('imagens/Empresarial.png'), size=(200, 72))
            self.img_label1_1 = ctk.CTkLabel(self.square1_1, image=self.img1_1, text="")
            self.img_label1_1.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_1_1 = ctk.CTkLabel(self.square1_1, text="ARBITRAGEM EMPRESARIAL", font=("Calibri", 15))
            self.h2_1_1.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button1_1 = ctk.CTkButton(self.square1_1, text="Contrate", command=partial(self.choose_contract,"Câmara de Arbitragem","Arbitragem Empresarial"), **botao)
            self.button1_1.pack(side=ctk.BOTTOM, pady=(0, 45))

            self.square1_2 = ctk.CTkFrame(self.frame_camara_arbitragem, **card)
            self.square1_2.grid(row = 0,column=1,padx = 50,pady = 20)
            self.square1_2.pack_propagate(False)
            #Imagem
            self.img1_2 = ctk.CTkImage(Image.open('imagens/Arbitragem.png'), size=(200, 72))
            self.img_label1_2 = ctk.CTkLabel(self.square1_2, image=self.img1_2, text="")
            self.img_label1_2.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_1_2 = ctk.CTkLabel(self.square1_2, text="ARBITRAGEM TRIBUTÁRIA", font=("Calibri", 15))
            self.h2_1_2.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button1_2 = ctk.CTkButton(self.square1_2, text="Contrate", command=partial(self.choose_contract,"Câmara de Arbitragem","Arbitragem Tributária"), **botao)
            self.button1_2.pack(side=ctk.BOTTOM, pady=(0, 45))

            self.square1_3 = ctk.CTkFrame(self.frame_camara_arbitragem, **card)
            self.square1_3.grid(row = 0,column=2,padx = 20,pady = 20)
            self.square1_3.pack_propagate(False)
            #Imagem
            self.img1_3 = ctk.CTkImage(Image.open('imagens/Editar.png'), size=(200, 72))
            self.img_label1_3 = ctk.CTkLabel(self.square1_3, image=self.img1_3, text="")
            self.img_label1_3.pack(side=ctk.TOP, pady=(20, 0))
            #Título
            self.h2_1_3 = ctk.CTkLabel(self.square1_3, text="Minutas Arbitral", font=("Calibri", 15))
            self.h2_1_3.pack(side=ctk.TOP, pady=(12, 0))
            #Botão
            self.button1_3 = ctk.CTkButton(self.square1_3, text="Contratar", command=partial(self.choose_contract,"Câmara de Arbitragem","Contrato Editável Arbitragem"), **botao)
            self.button1_3.pack(side=ctk.BOTTOM, pady=(0, 45))


            #Frame para ajustar o tamanho da tela
            self.frame_auxiliar = ctk.CTkFrame(self.body_frame, height=0, width=2100,**self.framePrincipal)
            self.frame_auxiliar.pack(pady=(50, 50), padx=(0,0))

            # Adiciona evento de redimensionamento da janela
            self.bind("<Configure>", self.on_window_resize)