import tkinter
from tkinter import ttk
import customtkinter
from PIL import Image


class telaPrincipal:
    def __init__(self,root):
        customtkinter.set_default_color_theme("lib/temaTkinterCustom.json")

        self.janela = root
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
        
        # Usuario teste
        usuario = usuarioModel(nome="João Caio", sobrenome="Pereira", email="email@exemplo.com", telefone="123456789", pais="Brasil", cargo="Desenvolvedor")

        # Nome do usuario no cabeçalho
        self.nome_usuario_label = customtkinter.CTkLabel(self.cabecalho, text=f"{usuario.nome} {usuario.sobrenome}")
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

        #Consultoria Empresarial

        #Título
        self.H1_consultoria_empresarial = customtkinter.CTkLabel(self.body_frame, text="Consultoria Empresarial", font=("Consolas", 40))
        self.H1_consultoria_empresarial.pack(side=customtkinter.TOP, pady=(80 ,0))
        
        #Frame
        self.frame_consultoria_empresarial = customtkinter.CTkFrame(self.body_frame, height=280, width=950)
        self.frame_consultoria_empresarial.pack(pady=(40, 0))

        
        # Card customizado
        card = {
            "corner_radius": 20,  # Adiciona um raio de canto de 10
            "width": 230,   # Largura
            "height": 230,  # Altura
            "fg_color": "#EFEFEF",  # Cor de fundo do quadrado
            "border_width": 2,
            "border_color": "#00343D",  # Cor da borda
        }

        #Primeira linha
        self.square1_1 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square1_1.place(x=50, y=25)

        self.square1_2 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square1_2.place(x=350, y=25)

        self.square1_3 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square1_3.place(x=650, y=25)

        #Segunda linha
        self.square2_1 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square2_1.place(x=50, y=70)

        self.square2_2 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square2_2.place(x=350, y=90)

        self.square2_3 = customtkinter.CTkFrame(self.frame_consultoria_empresarial, **card)
        self.square2_3.place(x=650, y=220)

        #Consultoria Tributária

        #Título
        self.H1_consultoria_tributaria = customtkinter.CTkLabel(self.body_frame, text="Consultoria Tributária", font=("Consolas", 40))
        self.H1_consultoria_tributaria.pack(side=customtkinter.TOP, pady=(90 ,0))
        #Frame 
        self.frame_consultoria_tributaria = customtkinter.CTkFrame(self.body_frame, height=280, width=950)
        self.frame_consultoria_tributaria.pack(pady=(40, 0))

        #Primeira linha
        self.square1_1 = customtkinter.CTkFrame(self.frame_consultoria_tributaria, **card)
        self.square1_1.place(x=50, y=25)

        self.square1_2 = customtkinter.CTkFrame(self.frame_consultoria_tributaria, **card)
        self.square1_2.place(x=350, y=25)

        self.square1_3 = customtkinter.CTkFrame(self.frame_consultoria_tributaria, **card)
        self.square1_3.place(x=650, y=25)

        #Câmara de Arbitragem

        #Título
        self.H1_camara_arbitragem = customtkinter.CTkLabel(self.body_frame, text="Câmara de Arbitragem", font=("Consolas", 40))
        self.H1_camara_arbitragem.pack(side=customtkinter.TOP, pady=(90 ,0))
        #Frame
        self.frame_camara_arbitragem = customtkinter.CTkFrame(self.body_frame, height=280, width=950)
        self.frame_camara_arbitragem.pack(pady=(40, 0))

        #Primeira linha
        self.square1_1 = customtkinter.CTkFrame(self.frame_camara_arbitragem, **card)
        self.square1_1.place(x=50, y=25)

        self.square1_2 = customtkinter.CTkFrame(self.frame_camara_arbitragem, **card)
        self.square1_2.place(x=350, y=25)

        self.square1_3 = customtkinter.CTkFrame(self.frame_camara_arbitragem, **card)
        self.square1_3.place(x=650, y=25)

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