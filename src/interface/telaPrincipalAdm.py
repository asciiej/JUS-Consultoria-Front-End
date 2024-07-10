from tkinter import ttk
import customtkinter
from PIL import Image
from ..utilitarios.user_session import USER_SESSION
from src.interface.edicaoContratos import telaEdicaoContrato
from src.interface.alterarAcesso import alterarAcesso
from functools import partial


class telaPrincipalAdm:
    def __init__(self,janela,controlers : dict):
        self.controlers = controlers
        customtkinter.set_default_color_theme("lib/temaTkinterCustom.json")

        self.janela = janela
        self.janela.title('JUS Consultorias')
        self.font = customtkinter.CTkFont('Helvetica',14)

        # Cabeçalho menu personalizado
        cabecalho_menu = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#6EC1E4", "#6EC1E4"]
        }

        # Cabeçalho
        self.cabecalho = customtkinter.CTkFrame(self.janela, height=104, **cabecalho_menu)
        self.cabecalho.pack(fill=customtkinter.X)

        # Logo
        self.logoJUS = customtkinter.CTkImage(Image.open('imagens/Logomarca JUS.png'),size = (80,72.54))
        self.logo_cabecalho = customtkinter.CTkLabel(self.cabecalho, image=self.logoJUS, text = "")
        self.logo_cabecalho.pack(side=customtkinter.LEFT, padx=(18, 0), pady=7)

        # Usuario foto
        self.userPic = customtkinter.CTkImage(Image.open('imagens/User Male Black.png'), size = (90,90))
        self.userPic_cabecalho = customtkinter.CTkLabel(self.cabecalho, image=self.userPic, text = "")
        self.userPic_cabecalho.pack(side=customtkinter.RIGHT, padx=(0, 18), pady=7)

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

        self.botao_consultoria_empresarial = customtkinter.CTkButton(self.cabecalho, text="Consultoria Empresarial", command=self.click_consultoria_empresarial, **opcao_menu)
        self.botao_consultoria_empresarial.pack(side=customtkinter.LEFT, padx=(25,0))

        self.botao_consultoria_tributaria = customtkinter.CTkButton(self.cabecalho, text="Consultoria Tributária", command=self.click_consultoria_tributaria, **opcao_menu)
        self.botao_consultoria_tributaria.pack(side=customtkinter.LEFT, padx=(25,0))

        self.botao_camara_arbitragem = customtkinter.CTkButton(self.cabecalho, text="Câmara de Arbitragem", command=self.click_camara_arbitragem, **opcao_menu)
        self.botao_camara_arbitragem.pack(side=customtkinter.LEFT, padx=(25,0))

        # Nome do usuario no cabeçalho
        self.nome_usuario_label = customtkinter.CTkLabel(self.cabecalho, text=f"{USER_SESSION.get_user_data().nome} {USER_SESSION.get_user_data().sobrenome}", font=self.font)
        self.nome_usuario_label.pack(side=customtkinter.RIGHT, padx=(0, 25))

        # Calcular a altura do "body"
        window_width = self.janela.winfo_width()
        window_height = self.janela.winfo_height()
        header_height = self.cabecalho.winfo_height()
        body_height = window_height - header_height

        body = {
            "corner_radius": 0,
            "border_width": 0,
            "fg_color": ["#EFEFEF", "#EFEFEF"]

        }

        #Barra Scroll
        self.canvas = customtkinter.CTkCanvas(self.janela, height=body_height)
        self.canvas.pack(side=customtkinter.LEFT, fill=customtkinter.BOTH, expand=True)

        #Body da pagina
        self.body_frame = customtkinter.CTkFrame(self.canvas, **body)
        self.body_frame.pack(fill=customtkinter.BOTH)

        #Adicionando scrollbar vertical
        self.vertical_scrollbar = ttk.Scrollbar(self.janela, orient="vertical", command=self.canvas.yview)
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
        self.buttonAlterarAcesso = customtkinter.CTkButton(self.body_frame,text="Alterar nível de acesso de usuário",command=self.alterarNivelAcesso,width=400,height=50)
        self.buttonAlterarAcesso.pack(side=customtkinter.TOP, pady=(80 ,20))

        #Consultoria Empresarial
        #Título
        self.H1_consultoria_empresarial = customtkinter.CTkLabel(self.body_frame, text="Consultoria Empresarial", font=("Consolas", 40))
        self.H1_consultoria_empresarial.pack(side=customtkinter.TOP, pady=(80 ,20))

        #Frame
        self.frame_consultoria_empresarial = customtkinter.CTkScrollableFrame(self.body_frame, height=280, width=900)
        self.frame_consultoria_empresarial.pack()

    #Primeira linha
        self.square1_1 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square1_1.grid(row = 0,column=0,padx = 20,pady = 20)
        self.square1_1.pack_propagate(False)
        #Imagem
        self.img1_1 = customtkinter.CTkImage(Image.open('imagens/Profissional.png'), size=(200, 72))
        self.img_label1_1 = customtkinter.CTkLabel(self.square1_1, image=self.img1_1, text="")
        self.img_label1_1.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_1_1 = customtkinter.CTkLabel(self.square1_1, text="CONTRATO DE PRESTAÇÃO DE\nSERVIÇOS PROFISSIONAIS", font=("Calibri", 15))
        self.h2_1_1.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button1_1 = customtkinter.CTkButton(self.square1_1, text="Edite", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Prestação de Serviços Profissionais"), **botao)
        self.button1_1.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        self.square1_2 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square1_2.grid(row = 0,column=1,padx = 50,pady = 20)
        self.square1_2.pack_propagate(False)
        #Imagem
        self.img1_2 = customtkinter.CTkImage(Image.open('imagens/Hospitalar.png'), size=(200, 72))
        self.img_label1_2 = customtkinter.CTkLabel(self.square1_2, image=self.img1_2, text="")
        self.img_label1_2.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_1_2 = customtkinter.CTkLabel(self.square1_2, text="CONTRATO DE PRESTAÇÃO DE\nSERVIÇOS MÉDICO-HOSPITALAR", font=("Calibri", 15))
        self.h2_1_2.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button1_2 = customtkinter.CTkButton(self.square1_2, text="Edite", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Prestação de Serviços Médico-Hospitalar"), **botao)
        self.button1_2.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        self.square1_3 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square1_3.grid(row = 0,column=2,padx = 20,pady = 20)
        self.square1_3.pack_propagate(False)
        #Imagem
        self.img1_3 = customtkinter.CTkImage(Image.open('imagens/Mercantil.png'), size=(200, 72))
        self.img_label1_3 = customtkinter.CTkLabel(self.square1_3, image=self.img1_3, text="")
        self.img_label1_3.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_1_3 = customtkinter.CTkLabel(self.square1_3, text="CONTRATO DE COMPRA E\nVENDA MERCANTIL", font=("Calibri", 15))
        self.h2_1_3.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button1_3 = customtkinter.CTkButton(self.square1_3, text="Edite", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Compra e Venda Mercantil"), **botao)
        self.button1_3.pack(side=customtkinter.BOTTOM, pady=(0, 45))


        #Segunda linha

        self.square2_1 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square2_1.grid(row = 1,column=0,padx= 20,pady = 20)
        self.square2_1.pack_propagate(False)
        #Imagem
        self.img2_1 = customtkinter.CTkImage(Image.open('imagens/Imovel.png'), size=(200, 72))
        self.img_label2_1 = customtkinter.CTkLabel(self.square2_1, image=self.img2_1, text="")
        self.img_label2_1.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_2_1 = customtkinter.CTkLabel(self.square2_1, text="CONTRATO DE COMPRA E\nVENDA DE IMÓVEL", font=("Calibri", 15))
        self.h2_2_1.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button2_1 = customtkinter.CTkButton(self.square2_1, text="Edite", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Compra e Venda de Imóvel"), **botao)
        self.button2_1.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        self.square2_2 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square2_2.grid(row = 1,column=1,padx = 20,pady = 20)
        self.square2_2.pack_propagate(False)
        #Imagem
        self.img2_2 = customtkinter.CTkImage(Image.open('imagens/LocacaoImovel.png'), size=(200, 72))
        self.img_label2_2 = customtkinter.CTkLabel(self.square2_2, image=self.img2_2, text="")
        self.img_label2_2.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_2_2 = customtkinter.CTkLabel(self.square2_2, text="CONTRATO DE LOCAÇÃO DE\nIMÓVEL", font=("Calibri", 15))
        self.h2_2_2.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button2_2 = customtkinter.CTkButton(self.square2_2, text="Edite",command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Locação de Imóvel"), **botao)
        self.button2_2.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        self.square2_3 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square2_3.grid(row = 1,column=2,padx = 20,pady = 20)
        self.square2_3.pack_propagate(False)
        #Imagem
        self.img2_3 = customtkinter.CTkImage(Image.open('imagens/Rural.png'), size=(200, 72))
        self.img_label2_3 = customtkinter.CTkLabel(self.square2_3, image=self.img2_3, text="")
        self.img_label2_3.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_2_3 = customtkinter.CTkLabel(self.square2_3, text="CONTRATO DE ARRENDAMENTO\nRURAL", font=("Calibri", 15))
        self.h2_2_3.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button2_3 = customtkinter.CTkButton(self.square2_3, text="Edite",command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Arrendamento Rural"), **botao)
        self.button2_3.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        #Terceira linha

        self.square3_1 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square3_1.grid(row = 2,column=0,padx= 20,pady = 20)
        self.square3_1.pack_propagate(False)
        #Imagem
        self.img3_1 = customtkinter.CTkImage(Image.open('imagens/Agricola.png'), size=(200, 72))
        self.img_label3_1 = customtkinter.CTkLabel(self.square3_1, image=self.img3_1, text="")
        self.img_label3_1.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_3_1 = customtkinter.CTkLabel(self.square3_1, text="CONTRATO DE PARCERIA\nAGRÍCOLA", font=("Calibri", 15))
        self.h2_3_1.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button3_1 = customtkinter.CTkButton(self.square3_1, text="Edite", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Parceria Agrícola"), **botao)
        self.button3_1.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        self.square3_2 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square3_2.grid(row = 2,column=1,padx = 20,pady = 20)
        self.square3_2.pack_propagate(False)
        #Imagem
        self.img3_2 = customtkinter.CTkImage(Image.open('imagens/Software.png'), size=(200, 72))
        self.img_label3_2 = customtkinter.CTkLabel(self.square3_2, image=self.img3_2, text="")
        self.img_label3_2.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_3_2 = customtkinter.CTkLabel(self.square3_2, text="CONTRATO DE LICENÇA DE USO\nDE SOFTWARE", font=("Calibri", 15))
        self.h2_3_2.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button3_2 = customtkinter.CTkButton(self.square3_2, text="Edite", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Licença de Uso de Software"), **botao)
        self.button3_2.pack(side=customtkinter.BOTTOM, pady=(0, 45))


    #Quarta linha

        self.square4_1 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square4_1.grid(row = 2,column=2,padx= 20,pady = 20)
        self.square4_1.pack_propagate(False)
        #Imagem
        self.img4_1 = customtkinter.CTkImage(Image.open('imagens/Intelectual.png'), size=(200, 72))
        self.img_label4_1 = customtkinter.CTkLabel(self.square4_1, image=self.img4_1, text="")
        self.img_label4_1.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_4_1 = customtkinter.CTkLabel(self.square4_1, text="CONTRATO DE LICENÇA E CESSÃO\nDE DIREITOS DE USO DE\nPROPRIEDADE INTELECTUAL", font=("Calibri", 15))
        self.h2_4_1.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button4_1 = customtkinter.CTkButton(self.square4_1, text="Edite", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Licença de Cessão de Direitos de Uso de Propriedade Intelectual"), **botao)
        self.button4_1.pack(side=customtkinter.BOTTOM, pady=(0, 36))

        self.square4_2 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square4_2.grid(row = 3,column=0,padx = 20,pady = 20)
        self.square4_2.pack_propagate(False)
        #Imagem
        self.img4_2 = customtkinter.CTkImage(Image.open('imagens/Franquia.png'), size=(200, 72))
        self.img_label4_2 = customtkinter.CTkLabel(self.square4_2, image=self.img4_2, text="")
        self.img_label4_2.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_4_2 = customtkinter.CTkLabel(self.square4_2, text="CONTRATO DE FRANQUIA", font=("Calibri", 15))
        self.h2_4_2.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button4_2 = customtkinter.CTkButton(self.square4_2, text="Edite", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Franquia"), **botao)
        self.button4_2.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        self.square4_3 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square4_3.grid(row = 3,column=1,padx = 20,pady = 20)
        self.square4_3.pack_propagate(False)
        #Imagem
        self.img4_3 = customtkinter.CTkImage(Image.open('imagens/Indeterminado.png'), size=(200, 72))
        self.img_label4_3 = customtkinter.CTkLabel(self.square4_3, image=self.img4_3, text="")
        self.img_label4_3.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_4_3 = customtkinter.CTkLabel(self.square4_3, text="CONTRATO DE TRABALHO POR\nPRAZO INDETERMINADO", font=("Calibri", 15))
        self.h2_4_3.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button4_3 = customtkinter.CTkButton(self.square4_3, text="Edite", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato de Trabalho por Prazo Indeterminado"), **botao)
        self.button4_3.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        self.square5_1 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square5_1.grid(row = 3,column=2,padx = 20,pady = 20)
        self.square5_1.pack_propagate(False)
        #Imagem
        self.img5_1 = customtkinter.CTkImage(Image.open('imagens/Editar.png'), size=(200, 72))
        self.img_label5_1 = customtkinter.CTkLabel(self.square5_1, image=self.img5_1, text="")
        self.img_label5_1.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_5_1 = customtkinter.CTkLabel(self.square5_1, text="Contrato Editável", font=("Calibri", 15))
        self.h2_5_1.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button5_1 = customtkinter.CTkButton(self.square5_1, text="Contratar", command=partial(self.choose_contract,"Consultoria Empresarial","Contrato Editável Empresarial"), **botao)
        self.button5_1.pack(side=customtkinter.BOTTOM, pady=(0, 45))


        #Consultoria Tributária

        #Título
        self.H1_consultoria_tributaria = customtkinter.CTkLabel(self.body_frame, text="Consultoria Tributária", font=("Consolas", 40))
        self.H1_consultoria_tributaria.pack(side=customtkinter.TOP, pady=(90 ,0))
        #Frame
        self.frame_consultoria_tributaria = customtkinter.CTkFrame(self.body_frame, height=280, width=950)
        self.frame_consultoria_tributaria.pack(pady=(40, 0))


        #Primeira linha

        self.square1_1 = customtkinter.CTkFrame(self.frame_consultoria_tributaria, **card)
        self.square1_1.grid(row = 0,column=0,padx = 20,pady = 20)
        self.square1_1.pack_propagate(False)
        #Imagem
        self.img1_1 = customtkinter.CTkImage(Image.open('imagens/Tributario.png'), size=(200, 72))
        self.img_label1_1 = customtkinter.CTkLabel(self.square1_1, image=self.img1_1, text="")
        self.img_label1_1.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_1_1 = customtkinter.CTkLabel(self.square1_1, text="PARECER TRIBUTÁRIO", font=("Calibri", 15))
        self.h2_1_1.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button1_1 = customtkinter.CTkButton(self.square1_1, text="Edite", command=partial(self.choose_contract,"Consultoria Tributária","Parecer Tributário"), **botao)
        self.button1_1.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        self.square1_2 = customtkinter.CTkFrame(self.frame_consultoria_tributaria, **card)
        self.square1_2.grid(row = 0,column=1,padx = 50,pady = 20)
        self.square1_2.pack_propagate(False)
        #Imagem
        self.img1_2 = customtkinter.CTkImage(Image.open('imagens/Planejamento.png'), size=(200, 72))
        self.img_label1_2 = customtkinter.CTkLabel(self.square1_2, image=self.img1_2, text="")
        self.img_label1_2.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_1_2 = customtkinter.CTkLabel(self.square1_2, text="PLANEJAMENTO TRIBUTÁRIO", font=("Calibri", 15))
        self.h2_1_2.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button1_2 = customtkinter.CTkButton(self.square1_2, text="Edite", command=partial(self.choose_contract,"Consultoria Tributária","Planejamento Tributário"), **botao)
        self.button1_2.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        self.square1_3 = customtkinter.CTkFrame(self.frame_consultoria_tributaria, **card)
        self.square1_3.grid(row = 0,column=2,padx = 20,pady = 20)
        self.square1_3.pack_propagate(False)
        #Imagem
        self.img1_3 = customtkinter.CTkImage(Image.open('imagens/Editar.png'), size=(200, 72))
        self.img_label1_3 = customtkinter.CTkLabel(self.square1_3, image=self.img1_3, text="")
        self.img_label1_3.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_1_3 = customtkinter.CTkLabel(self.square1_3, text="Contrato Editável", font=("Calibri", 15))
        self.h2_1_3.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button1_3 = customtkinter.CTkButton(self.square1_3, text="Edite", command=partial(self.choose_contract,"Consultoria Tributária","Contrato Editável Tributária"), **botao)
        self.button1_3.pack(side=customtkinter.BOTTOM, pady=(0, 45))

    

        #Câmara de Arbitragem

        #Título
        self.H1_camara_arbitragem = customtkinter.CTkLabel(self.body_frame, text="Câmara de Arbitragem", font=("Consolas", 40))
        self.H1_camara_arbitragem.pack(side=customtkinter.TOP, pady=(90 ,0))
        #Frame
        self.frame_camara_arbitragem = customtkinter.CTkFrame(self.body_frame, height=280, width=950)
        self.frame_camara_arbitragem.pack(pady=(40, 0))

        #Primeira linha

        self.square1_1 = customtkinter.CTkFrame(self.frame_camara_arbitragem, **card)
        self.square1_1.grid(row = 0,column=0,padx = 20,pady = 20)
        self.square1_1.pack_propagate(False)
        #Imagem
        self.img1_1 = customtkinter.CTkImage(Image.open('imagens/Empresarial.png'), size=(200, 72))
        self.img_label1_1 = customtkinter.CTkLabel(self.square1_1, image=self.img1_1, text="")
        self.img_label1_1.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_1_1 = customtkinter.CTkLabel(self.square1_1, text="ARBITRAGEM EMPRESARIAL", font=("Calibri", 15))
        self.h2_1_1.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button1_1 = customtkinter.CTkButton(self.square1_1, text="Edite", command=partial(self.choose_contract,"Câmara de Arbitragem","Arbitragem Empresarial"), **botao)
        self.button1_1.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        self.square1_2 = customtkinter.CTkFrame(self.frame_camara_arbitragem, **card)
        self.square1_2.grid(row = 0,column=1,padx = 50,pady = 20)
        self.square1_2.pack_propagate(False)
        #Imagem
        self.img1_2 = customtkinter.CTkImage(Image.open('imagens/Arbitragem.png'), size=(200, 72))
        self.img_label1_2 = customtkinter.CTkLabel(self.square1_2, image=self.img1_2, text="")
        self.img_label1_2.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_1_2 = customtkinter.CTkLabel(self.square1_2, text="ARBITRAGEM TRIBUTÁRIA", font=("Calibri", 15))
        self.h2_1_2.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button1_2 = customtkinter.CTkButton(self.square1_2, text="Edite", command=partial(self.choose_contract,"Câmara de Arbitragem","Arbitragem Tributária"), **botao)
        self.button1_2.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        self.square1_3 = customtkinter.CTkFrame(self.frame_camara_arbitragem, **card)
        self.square1_3.grid(row = 0,column=2,padx = 20,pady = 20)
        self.square1_3.pack_propagate(False)
        #Imagem
        self.img1_3 = customtkinter.CTkImage(Image.open('imagens/Editar.png'), size=(200, 72))
        self.img_label1_3 = customtkinter.CTkLabel(self.square1_3, image=self.img1_3, text="")
        self.img_label1_3.pack(side=customtkinter.TOP, pady=(20, 0))
        #Título
        self.h2_1_3 = customtkinter.CTkLabel(self.square1_3, text="Contrato Editável", font=("Calibri", 15))
        self.h2_1_3.pack(side=customtkinter.TOP, pady=(12, 0))
        #Botão
        self.button1_3 = customtkinter.CTkButton(self.square1_3, text="Edite", command=partial(self.choose_contract,"Câmara de Arbitragem","Contrato Editável Arbitragem"), **botao)
        self.button1_3.pack(side=customtkinter.BOTTOM, pady=(0, 45))

        #Frame para ajustar o tamanho da tela
        self.frame_auxiliar = customtkinter.CTkFrame(self.body_frame, height=0, width=2100)
        self.frame_auxiliar.pack(pady=(50, 50), padx=(0,0))


        # Adiciona evento de redimensionamento da janela
        self.janela.bind("<Configure>", self.on_window_resize)
        self.janela.mainloop()

    def click_consultoria_empresarial(self):
        self.canvas.yview_moveto((self.H1_consultoria_empresarial.winfo_y() - 150  ) / self.body_frame.winfo_height())

    def click_consultoria_tributaria(self):
        self.canvas.yview_moveto((self.H1_consultoria_tributaria.winfo_y() - 100) / self.body_frame.winfo_height())

    def click_camara_arbitragem(self):
        self.canvas.yview_moveto((self.H1_camara_arbitragem.winfo_y() - 100) / self.body_frame.winfo_height())

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

    def choose_contract(self,tipo,titulo):
        self.janela.unbind("<Configure>")
        for widget in self.janela.winfo_children():
            widget.destroy()
        telaEdicaoContrato(self.janela,self.controlers,titulo,tipo)
    
    def alterarNivelAcesso(self):
        self.janela.unbind("<Configure>")
        for widget in self.janela.winfo_children():
            widget.destroy()
        alterarAcesso(self.janela)